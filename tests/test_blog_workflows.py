"""Offline workflow coverage for installation, banners and CDN artifacts."""

import hashlib
import io
import json
import subprocess
import tarfile
import tempfile
import unittest
from email.message import Message
from pathlib import Path
from unittest import mock
from urllib.error import URLError

from scripts import banners, publishing, runtime


class InstallationTests(unittest.TestCase):
    def fixture(self, root):
        for name, version in (("hugo", "0.148.2"), ("prettier", "3.9.6")):
            (root / f".{name}-version").write_text(version)
        return runtime.Tools(root)

    def executable(self, path, output):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"#!/bin/sh\necho '{output}'\n")
        path.chmod(0o755)

    def test_empty_cache_installs_pins_then_reuses_them_offline(self):
        for system, machine, asset in (
            ("Darwin", "arm64", "darwin-universal"),
            ("Linux", "x86_64", "linux-amd64"),
            ("Linux", "aarch64", "linux-arm64"),
        ):
            with (
                self.subTest(platform=asset),
                tempfile.TemporaryDirectory() as directory,
            ):
                tools = self.fixture(Path(directory))
                payload = b"#!/bin/sh\necho 'hugo v0.148.2'\n"
                archive = io.BytesIO()
                with tarfile.open(fileobj=archive, mode="w:gz") as tar:
                    member = tarfile.TarInfo("hugo")
                    member.size = len(payload)
                    tar.addfile(member, io.BytesIO(payload))
                data = archive.getvalue()
                name = f"hugo_0.148.2_{asset}.tar.gz"

                def download(url, **kwargs):
                    if url.endswith("_checksums.txt"):
                        return io.BytesIO(
                            f"{hashlib.sha256(data).hexdigest()}  {name}\n".encode()
                        )
                    self.assertTrue(url.endswith("/" + name))
                    return io.BytesIO(data)

                actual_run = subprocess.run

                def run(args, **kwargs):
                    if args[0] == "npm":
                        self.assertIn("prettier@3.9.6", args)
                        self.assertIn("--ignore-scripts", args)
                        self.executable(tools.candidate("prettier"), "3.9.6")
                        return subprocess.CompletedProcess(args, 0)
                    return actual_run(args, **kwargs)

                with (
                    mock.patch.object(runtime.platform, "system", return_value=system),
                    mock.patch.object(
                        runtime.platform, "machine", return_value=machine
                    ),
                    mock.patch.object(
                        runtime.shutil,
                        "which",
                        side_effect=lambda name: "npm" if name == "npm" else None,
                    ),
                    mock.patch.object(
                        runtime, "urlopen", side_effect=download
                    ) as network,
                    mock.patch.object(
                        runtime.subprocess, "run", side_effect=run
                    ) as processes,
                ):
                    tools.setup()
                    self.assertEqual(
                        tools.resolve("hugo"), str(tools.candidate("hugo"))
                    )
                    self.assertEqual(
                        tools.resolve("prettier"), str(tools.candidate("prettier"))
                    )
                    calls = network.call_count
                    npm_calls = sum(
                        c.args[0][0] == "npm" for c in processes.call_args_list
                    )
                    tools.setup()
                    self.assertEqual(network.call_count, calls)
                    self.assertEqual(
                        sum(c.args[0][0] == "npm" for c in processes.call_args_list),
                        npm_calls,
                    )
                    self.assertEqual(calls, 2)
                    self.assertEqual(npm_calls, 1)

    def test_checksum_failure_never_replaces_existing_binary(self):
        with tempfile.TemporaryDirectory() as directory:
            tools = self.fixture(Path(directory))
            target = tools.candidate("hugo")
            self.executable(target, "old")
            before = target.read_bytes()
            with (
                mock.patch.object(runtime.platform, "system", return_value="Darwin"),
                mock.patch.object(
                    runtime,
                    "urlopen",
                    side_effect=[
                        io.BytesIO(b"corrupted"),
                        io.BytesIO(b"bad  hugo_0.148.2_darwin-universal.tar.gz"),
                    ],
                ),
            ):
                with self.assertRaisesRegex(ValueError, "校验失败"):
                    tools.install_hugo(target)
            self.assertEqual(target.read_bytes(), before)

    def test_matching_system_tools_require_no_install(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tools = self.fixture(root)
            for name, output in (("hugo", "hugo v0.148.2"), ("prettier", "3.9.6")):
                self.executable(root / name, output)
            with (
                mock.patch.object(
                    runtime.shutil, "which", side_effect=lambda name: str(root / name)
                ),
                mock.patch.object(runtime, "urlopen") as network,
            ):
                tools.setup()
                self.assertEqual(tools.resolve("hugo"), str(root / "hugo"))
                self.assertEqual(tools.resolve("prettier"), str(root / "prettier"))
                network.assert_not_called()


class BannerWorkflowTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        patch = mock.patch.object(banners, "ROOT", self.root)
        patch.start()
        self.addCleanup(patch.stop)
        self.post = self.root / "2026-10-19-test.md"
        self.post.write_text('[example](https://example.com/page "!banner")\n')

    def response(self, body, url, content_type):
        response = io.BytesIO(body)
        response.geturl = lambda: url
        response.headers = Message()
        response.headers["Content-Type"] = content_type
        return response

    def test_fetch_update_cache_and_recover_missing_image(self):
        page = b'<meta property="og:image" content="/cover.png"><meta property="og:description" content="hello  &amp; world">'

        def fetch(request, **kwargs):
            url = request.full_url
            return self.response(
                page if url.endswith("/page") else b"image bytes",
                url,
                "text/html; charset=utf-8" if url.endswith("/page") else "image/png",
            )

        with mock.patch.object(banners, "urlopen", side_effect=fetch) as network:
            self.assertTrue(banners.update_file(self.post))
            self.assertEqual(network.call_count, 2)
            self.assertIn("hello &amp; world", self.post.read_text())
            images = list((self.root / "static/images/202610").glob("*.png"))
            self.assertEqual(len(images), 1)
            before = self.post.read_bytes()
            self.assertTrue(banners.update_file(self.post))
            self.assertEqual(network.call_count, 2)
            self.assertEqual(self.post.read_bytes(), before)
            images[0].unlink()
            self.assertTrue(banners.update_file(self.post))
            self.assertEqual(network.call_count, 3)
            self.assertEqual(images[0].read_bytes(), b"image bytes")

    def test_failed_page_refresh_preserves_existing_marker(self):
        before = self.post.read_bytes()
        with mock.patch.object(banners, "urlopen", side_effect=URLError("offline")):
            self.assertFalse(banners.update_file(self.post, refresh=True))
        self.assertEqual(self.post.read_bytes(), before)

    def test_fenced_examples_do_not_fetch(self):
        self.post.write_text("```markdown\n" + self.post.read_text() + "```\n")
        before = self.post.read_bytes()
        with mock.patch.object(banners, "urlopen") as network:
            self.assertTrue(banners.update_file(self.post))
            network.assert_not_called()
        self.assertEqual(self.post.read_bytes(), before)

    def test_youtube_oembed_fallback_omits_generic_description(self):
        with mock.patch.object(
            banners,
            "fetch",
            side_effect=[
                (
                    b'<meta name="description" content="generic service">',
                    "https://www.youtube.com/watch?v=x",
                    "text/html",
                    "utf-8",
                ),
                (
                    json.dumps(
                        {"thumbnail_url": "https://img.example/video.jpg"}
                    ).encode(),
                    "https://www.youtube.com/oembed",
                    "application/json",
                    "utf-8",
                ),
            ],
        ):
            result = banners.page_metadata("https://youtu.be/x")
        self.assertEqual(result["image_url"], "https://img.example/video.jpg")
        self.assertEqual(result["description"], "")


class ArtifactWorkflowTests(unittest.TestCase):
    def test_bulk_conversion_preserves_binary_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = {
                "index.html": '<img src="/images/a.png">',
                "rss.xml": "<rss>&lt;img src=&quot;/images/a.png&quot;&gt;</rss>",
                "post.md": "![a](/images/a.png)",
                "index.json": '{"image":"/images/a.png"}',
            }
            for name, source in sources.items():
                (root / name).write_text(source)
            binary = b"\x89PNG\xff/images/a.png"
            (root / "a.png").write_bytes(binary)
            config = {
                "site_url": "https://blog.example",
                "cdn_url": "https://cdn.example",
            }
            self.assertEqual(publishing.cdn_artifacts(root, config), 4)
            for name in sources:
                self.assertIn("https://cdn.example/a.png", (root / name).read_text())
            self.assertEqual(
                json.loads((root / "index.json").read_text())["image"],
                "https://cdn.example/a.png",
            )
            self.assertEqual((root / "a.png").read_bytes(), binary)
            self.assertEqual(publishing.cdn_artifacts(root, config), 0)
