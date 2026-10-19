"""Regressions for author data boundaries and publication output."""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
import tempfile
import unittest
from email.message import Message
from pathlib import Path
from unittest import mock
from urllib.error import HTTPError

from scripts import cli, images, publishing
from scripts.git import ZERO, Repository
from scripts.runtime import Tools


class GitFilesTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo = Repository(self.root)
        self.repo.git("init", "-q")
        self.repo.git("config", "user.name", "Test")
        self.repo.git("config", "user.email", "test@example.com")
        self.repo.git("config", "core.hooksPath", "/dev/null")
        self.repo.git("config", "commit.gpgsign", "false")
        self.write("note.md", "initial\n")
        self.commit()
        self.base = self.repo.git("rev-parse", "HEAD").decode().strip()
        self.repo.git("update-ref", "refs/remotes/origin/master", self.base)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit(self):
        self.repo.git("add", "--all")
        self.repo.git("commit", "-qm", "fixture")

    def test_worktree_handles_untracked_directories_spaces_and_deleted_files(self):
        self.write("static/images/new folder/a.png", "image")
        self.write("notes/中文 name.md", "hello")
        (self.root / "note.md").unlink()
        self.assertEqual(
            self.repo.files(), ["notes/中文 name.md", "static/images/new folder/a.png"]
        )

    def test_staged_snapshot_preserves_unstaged_content_and_index(self):
        self.write("note.md", "staged\n")
        self.repo.git("add", "note.md")
        self.write("note.md", "staged\nprivate draft\n")
        self.write("untracked.md", "not staged")
        before = self.repo.git("diff", "--cached")
        with self.repo.snapshot(paths=self.repo.files("staged")) as snapshot:
            self.assertEqual((snapshot / "note.md").read_text(), "staged\n")
            self.assertFalse((snapshot / "untracked.md").exists())
        self.assertEqual(before, self.repo.git("diff", "--cached"))
        self.assertIn("private draft", (self.root / "note.md").read_text())

    def test_format_never_restages_working_content(self):
        self.write("note.md", "staged\n")
        self.repo.git("add", "note.md")
        self.write("note.md", "staged\nprivate draft\n")
        before = self.repo.git("diff", "--cached")
        formatter = self.root / "formatter"
        formatter.write_text(
            f"#!{sys.executable}\nfrom pathlib import Path\nPath('note.md').write_text('formatted private draft\\n')\n"
        )
        formatter.chmod(0o755)
        tools = mock.Mock()
        tools.resolve.return_value = str(formatter)
        self.assertTrue(cli.format_files(self.root, ["note.md"], tools, write=True))
        self.assertEqual(before, self.repo.git("diff", "--cached"))
        self.assertEqual(
            (self.root / "note.md").read_text(), "formatted private draft\n"
        )

    def test_staged_check_ignores_unstaged_remote_image_and_handles_staged_config(self):
        self.write(".prettierrc", "{}")
        self.write("note.md", "![local](/images/202610/a.png)\n")
        self.repo.git("add", "--all")
        self.write("note.md", "![private](https://example.com/private.png)\n")
        with mock.patch.object(cli, "format_files", return_value=True):
            self.assertTrue(
                cli.check(
                    argparse.Namespace(scope="staged", base=None, changed_only=True),
                    self.repo,
                    Tools(self.root),
                )
            )

    def test_rename_uses_destination_and_deleted_file_is_excluded(self):
        self.repo.git("mv", "note.md", "new name.md")
        self.assertEqual(self.repo.files("staged"), ["new name.md"])

    def test_push_range_does_not_include_uncommitted_drafts(self):
        self.write("sent.md", "committed")
        self.commit()
        self.write("draft.md", "uncommitted")
        self.assertEqual(self.repo.files("push", self.base), ["sent.md"])
        self.assertEqual(self.repo.files(), ["draft.md"])

    def test_zero_base_checks_initial_push_and_invalid_base_fails(self):
        self.repo.git("update-ref", "-d", "refs/remotes/origin/master")
        self.assertEqual(self.repo.files("push", ZERO), ["note.md"])
        with self.assertRaises(ValueError):
            self.repo.files("push", "not-a-commit")

    def test_first_push_of_feature_branch_uses_master_baseline(self):
        self.write("feature.md", "new article")
        self.commit()
        self.assertEqual(self.repo.files("push", ZERO), ["feature.md"])

    def test_force_push_compares_tips_instead_of_merge_base(self):
        self.write("remote.md", "remote branch")
        self.commit()
        old_tip = self.repo.git("rev-parse", "HEAD").decode().strip()
        self.repo.git("checkout", "-q", "--detach", self.base)
        self.write("local.md", "new history")
        self.commit()
        # remote.md is deleted in the pushed result, not an existing file to check.
        self.assertEqual(self.repo.files("push", old_tip), ["local.md"])

    def test_push_hook_checks_pushed_ref_instead_of_current_checkout(self):
        self.write("sent.md", "committed snapshot")
        self.commit()
        tip = self.repo.git("rev-parse", "HEAD").decode().strip()
        self.repo.git("checkout", "-q", "--detach", self.base)
        self.write("private.md", "working draft")

        def inspect(snapshot, files, tools, full):
            self.assertEqual(files, ["sent.md"])
            self.assertEqual((snapshot / "sent.md").read_text(), "committed snapshot")
            self.assertNotIn("private.md", files)
            return True

        with (
            mock.patch(
                "sys.stdin",
                io.StringIO(
                    f"refs/heads/article {tip} refs/heads/article {self.base}\n"
                ),
            ),
            mock.patch.object(cli, "check_files", side_effect=inspect),
        ):
            self.assertTrue(cli.hook("pre-push", self.repo, mock.Mock()))

    def test_staged_file_survives_worktree_deletion(self):
        self.write("note.md", "indexed content")
        self.repo.git("add", "note.md")
        (self.root / "note.md").unlink()
        self.assertEqual(self.repo.files("staged"), ["note.md"])
        with self.repo.snapshot(paths=self.repo.files("staged")) as snapshot:
            self.assertEqual((snapshot / "note.md").read_text(), "indexed content")

    def test_first_push_hook_uses_master_and_pushed_snapshot(self):
        self.write("feature.md", "new article")
        self.commit()
        tip = self.repo.git("rev-parse", "HEAD").decode().strip()
        self.repo.git("checkout", "-q", "--detach", self.base)

        def inspect(snapshot, files, tools, full):
            self.assertEqual(files, ["feature.md"])
            self.assertEqual((snapshot / "feature.md").read_text(), "new article")
            return True

        with (
            mock.patch(
                "sys.stdin",
                io.StringIO(f"refs/heads/feature {tip} refs/heads/feature {ZERO}\n"),
            ),
            mock.patch.object(cli, "check_files", side_effect=inspect),
        ):
            self.assertTrue(cli.hook("pre-push", self.repo, mock.Mock()))


class ImageReferencesTests(unittest.TestCase):
    def test_markdown_references_collapsed_shortcut_and_balanced_url(self):
        source = "![one](https://example.com/a_(b).png)\n![two][Photo]\n![Photo][]\n![Photo]\n[photo]: <https://example.com/two.png>\n"
        self.assertEqual(
            [r.url for r in images.references(source)],
            ["https://example.com/a_(b).png", *["https://example.com/two.png"] * 3],
        )

    def test_multiline_html_quotes_and_srcset(self):
        source = "<img\n    src='https://example.com/a.png'\n    srcset='/images/a.png 1x, https://example.com/b.png 2x'>"
        self.assertEqual(
            [r.url for r in images.references(source)],
            ["https://example.com/a.png", "/images/a.png", "https://example.com/b.png"],
        )

    def test_fenced_and_inline_code_do_not_create_references(self):
        source = "```md\n![fake](https://example.com/code.png)\n```\n`![inline](https://example.com/inline.png)`\n![real](/images/202610/real.png)\n"
        self.assertEqual(
            [r.url for r in images.references(source)], ["/images/202610/real.png"]
        )

    def test_covers_banners_html_and_legacy_paths_do_not_swallow_surrounding_text(self):
        source = "---\ncover:\n  image: /images/202610/cover.png\ntitle: hello\n---\n<img src='/images/202610/html.png' alt='x'>\n[x](https://example.com \"!banner (/images/202610/banner.png) desc\")\n![old](../../static/images/upload_dropbox/201304/old.png)"
        refs = images.local_references(source)
        self.assertIn("202610/cover.png", refs)
        self.assertIn("202610/html.png", refs)
        self.assertIn("202610/banner.png", refs)
        self.assertIn("upload_dropbox/201304/old.png", refs)
        self.assertIn("2013/04/old.png", refs)
        self.assertNotIn("202611/cover.png", refs)

    def test_external_images_do_not_mark_local_images_as_used(self):
        self.assertEqual(
            images.local_references(
                "![external](https://elsewhere.example/images/202610/a.png)"
            ),
            set(),
        )

    def test_spaces_query_and_percent_encoded_paths(self):
        refs = images.local_references(
            "![x](</images/202610/a b.png?size=2>)\n![x](/images/202610/a%28b%29.png)"
        )
        self.assertIn("202610/a b.png", refs)
        self.assertIn("202610/a(b).png", refs)

    def test_same_basename_in_other_month_remains_unused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "content").mkdir()
            (root / "content/post.md").write_text("![x](/images/202610/a.png)")
            for month in ("202610", "202611"):
                folder = root / "static/images" / month
                folder.mkdir(parents=True)
                (folder / "a.png").write_bytes(b"fixture")
            self.assertEqual(
                images.unused_images(root),
                ["static/images/202611/a.png: 未被文章引用。"],
            )

    @mock.patch(
        "scripts.images.imagemagick", return_value=(["identify"], ["convert"])
    )
    def test_corrupt_and_later_oversized_frames_fail(self, _):
        with mock.patch(
            "scripts.images.subprocess.run",
            return_value=subprocess.CompletedProcess([], 1, "", "corrupt"),
        ):
            self.assertIn("无法读取", images.image_sizes(Path("/tmp"), ["bad.png"])[0])
        with mock.patch(
            "scripts.images.subprocess.run",
            return_value=subprocess.CompletedProcess([], 0, "10 20\n1001 20\n", ""),
        ):
            self.assertIn("超过", images.image_sizes(Path("/tmp"), ["animated.gif"])[0])

    def test_failed_resize_keeps_original_and_cleans_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.png").write_bytes(b"original")
            with mock.patch(
                "scripts.images.imagemagick",
                return_value=([], [sys.executable, "-c", "raise SystemExit(23)"]),
            ):
                with self.assertRaises(subprocess.CalledProcessError):
                    images.resize(root, ["a.png"])
            self.assertEqual((root / "a.png").read_bytes(), b"original")
            self.assertEqual(list(root.iterdir()), [root / "a.png"])


class PublicationTests(unittest.TestCase):
    def test_warmup_downloads_full_image_body_instead_of_head(self):
        response = mock.MagicMock()
        response.status = 200
        response.headers = Message()
        response.headers["Content-Type"] = "image/png"
        response.read.side_effect = [b"first chunk", b"second chunk", b""]
        opened = mock.MagicMock()
        opened.__enter__.return_value = response
        with mock.patch(
            "scripts.publishing.urlopen", return_value=opened
        ) as request:
            self.assertTrue(
                publishing.verify(
                    ["https://cdn.example/a.png"], attempts=1, download_images=True
                )
            )
            self.assertEqual(request.call_args.args[0].get_method(), "GET")
            self.assertEqual(response.read.call_count, 3)

    def test_warmup_rejects_200_html_and_empty_image(self):
        for content_type in ("text/html", "image/png"):
            response = mock.MagicMock()
            response.status = 200
            response.headers = Message()
            response.headers["Content-Type"] = content_type
            response.read.return_value = b""
            opened = mock.MagicMock()
            opened.__enter__.return_value = response
            with mock.patch("scripts.publishing.urlopen", return_value=opened):
                self.assertFalse(
                    publishing.verify(
                        ["https://cdn.example/a.png"], attempts=1, download_images=True
                    )
                )

    def test_warmup_rejects_truncated_image_body(self):
        response = mock.MagicMock()
        response.status = 200
        response.headers = Message()
        response.headers["Content-Type"] = "image/png"
        response.headers["Content-Length"] = "100"
        response.read.side_effect = [b"short", b""]
        opened = mock.MagicMock()
        opened.__enter__.return_value = response
        with mock.patch("scripts.publishing.urlopen", return_value=opened):
            self.assertFalse(
                publishing.verify(
                    ["https://cdn.example/a.png"], attempts=1, download_images=True
                )
            )

    def test_official_prefetch_signs_json_requests_and_batches_urls(self):
        opened = mock.MagicMock()
        opened.__enter__.return_value.read.return_value = (
            b'{"code":200,"requestId":"test-job"}'
        )
        urls = [f"https://cdn.example/{i}.png" for i in range(21)]
        with mock.patch(
            "scripts.publishing.urlopen", return_value=opened
        ) as request:
            publishing.prefetch_qiniu(urls + urls[:1], "test-access", "test-secret")
            self.assertEqual(request.call_count, 2)
            first = request.call_args_list[0].args[0]
            self.assertEqual(first.get_method(), "POST")
            self.assertEqual(
                first.full_url, "https://fusion.qiniuapi.com/v2/tune/prefetch"
            )
            self.assertEqual(
                first.get_header("Authorization"),
                "QBox test-access:Yxl77rTfBZMaA9SRZ49zZ4mC-Sk=",
            )
            self.assertEqual(json.loads(first.data)["urls"], urls[:20])
            self.assertEqual(
                json.loads(request.call_args_list[1].args[0].data)["urls"], urls[20:]
            )

    def test_official_prefetch_rejects_partial_api_failure(self):
        opened = mock.MagicMock()
        opened.__enter__.return_value.read.return_value = (
            b'{"code":200,"invalidUrls":["https://cdn.example/a.png"]}'
        )
        with mock.patch("scripts.publishing.urlopen", return_value=opened):
            with self.assertRaises(ValueError):
                publishing.prefetch_qiniu(
                    ["https://cdn.example/a.png"], "test-access", "test-secret"
                )

    def build_fixture(self, root):
        (root / "scripts").mkdir()
        (root / "scripts/publishing.json").write_text(
            json.dumps(
                {
                    "cdn_url": "https://cdn.example",
                    "s3_endpoint": "https://s3.example",
                    "s3_bucket": "test",
                }
            )
        )
        (root / "public").mkdir()
        (root / "public/index.html").write_text("previous successful build")
        (root / "public/old-hash.css").write_text("stale")
        tools = mock.Mock()
        tools.resolve.return_value = "/fixture/hugo"
        return tools

    def test_failed_build_preserves_previous_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tools = self.build_fixture(root)
            with (
                mock.patch.object(
                    publishing, "site_url", return_value="https://blog.example"
                ),
                mock.patch(
                    "scripts.cli.subprocess.run",
                    side_effect=subprocess.CalledProcessError(1, "hugo"),
                ),
            ):
                with self.assertRaises(subprocess.CalledProcessError):
                    cli.build(argparse.Namespace(cdn=False), Repository(root), tools)
            self.assertEqual(
                (root / "public/index.html").read_text(), "previous successful build"
            )
            self.assertTrue((root / "public/old-hash.css").exists())

    def test_successful_build_drops_stale_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tools = self.build_fixture(root)
            executable = root / "hugo"
            executable.write_text(
                f"#!{sys.executable}\nimport sys\nfrom pathlib import Path\nout = Path(sys.argv[sys.argv.index('--destination') + 1])\nout.mkdir()\n(out / 'index.html').write_text('new build')\n"
            )
            executable.chmod(0o755)
            tools.resolve.return_value = str(executable)
            with mock.patch.object(
                publishing, "site_url", return_value="https://blog.example"
            ):
                cli.build(argparse.Namespace(cdn=False), Repository(root), tools)
            self.assertEqual((root / "public/index.html").read_text(), "new build")
            self.assertFalse((root / "public/old-hash.css").exists())

    def test_verification_retries_transient_404_with_observation_times(self):
        success = mock.MagicMock()
        success.__enter__.return_value.status = 200
        url = "https://cdn.example/new.png"
        with (
            mock.patch(
                "scripts.publishing.urlopen",
                side_effect=[HTTPError(url, 404, "not ready", {}, None), success],
            ) as request,
            mock.patch("scripts.publishing.time.sleep") as sleep,
            mock.patch("sys.stdout", new_callable=io.StringIO) as output,
        ):
            self.assertTrue(publishing.verify([url], attempts=3, interval=1))
            self.assertEqual(request.call_count, 2)
            sleep.assert_called_once_with(1)
            self.assertIn("+00:00", output.getvalue())

    def test_cdn_rewrites_html_feed_markdown_banner_and_srcset(self):
        source = """<img src="/images/a.png"><a href='/images/a.png'>x</a>
&lt;img src=&#34;/images/feed.png&#34;&gt;
![x](/images/md.png)
[x](https://example.com "!banner (/images/card.png) desc")
[photo]: /images/ref.png
<img src="https://blog.alswl.com/images/abs.png" srcset="/images/a.png 1x,/images/b.png 2x">
<img src="https://other.example/images/external.png">"""
        output = publishing.rewrite_cdn(
            source, "https://blog.alswl.com", "https://cdn.example"
        )
        for name in ("a", "feed", "md", "card", "ref", "abs", "b"):
            self.assertIn(f"https://cdn.example/{name}.png", output)
        self.assertIn("https://other.example/images/external.png", output)
        self.assertEqual(
            publishing.rewrite_cdn(
                output, "https://blog.alswl.com", "https://cdn.example"
            ),
            output,
        )

    def test_local_cdn_build_is_rejected_before_any_write(self):
        with mock.patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                cli.build(argparse.Namespace(cdn=True), mock.Mock(), mock.Mock())

    def test_newer_installed_hugo_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "hugo"
            binary.write_text("#!/bin/sh\necho 'hugo v0.167.0'\n")
            binary.chmod(0o755)
            with mock.patch("scripts.runtime.shutil.which", return_value=str(binary)):
                self.assertEqual(Tools(root).resolve("hugo"), str(binary))


class WarmupWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.repo = mock.Mock(root=Path("/repo"))
        self.repo.files.return_value = [
            "static/images/202610/a b.png",
            "static/images/202610/icon.SVG",
            "content/post.md",
        ]
        self.args = argparse.Namespace(base="previous", attempts=4, interval=15)
        self.tools = mock.Mock()
        self.tools.resolve.return_value = "hugo"
        patches = {
            "config": mock.patch.object(
                publishing, "settings", return_value={"cdn_url": "https://cdn.example"}
            ),
            "site": mock.patch.object(
                publishing, "site_url", return_value="https://blog.example"
            ),
            "verify": mock.patch.object(publishing, "verify", return_value=True),
            "prefetch": mock.patch.object(publishing, "prefetch_qiniu"),
            "environment": mock.patch.dict("os.environ", {}, clear=True),
        }
        for name, patch in patches.items():
            setattr(self, name, patch.start())
            self.addCleanup(patch.stop)

    def test_no_credentials_waits_for_origin_before_canonical_get(self):
        self.assertTrue(cli.warm_images(self.args, self.repo, self.tools))
        calls = self.verify.call_args_list
        self.assertEqual(
            calls[0].args[0],
            [
                "https://blog.example/images/202610/a%20b.png",
                "https://blog.example/images/202610/icon.SVG",
            ],
        )
        self.assertEqual(
            calls[1].args[0],
            [
                "https://cdn.example/202610/a%20b.png",
                "https://cdn.example/202610/icon.SVG",
            ],
        )
        self.assertEqual(calls[1].kwargs, {"download_images": True})
        self.prefetch.assert_not_called()

    def test_origin_not_ready_never_requests_cdn(self):
        self.verify.return_value = False
        self.assertFalse(cli.warm_images(self.args, self.repo, self.tools))
        self.assertEqual(self.verify.call_count, 1)
        self.prefetch.assert_not_called()

    def test_no_changed_images_skips_all_network_requests(self):
        self.repo.files.return_value = ["content/post.md"]
        self.assertTrue(cli.warm_images(self.args, self.repo, self.tools))
        self.verify.assert_not_called()
        self.prefetch.assert_not_called()
        self.site.assert_not_called()

    @mock.patch.dict(
        "os.environ",
        {"QINIU_ACCESS_KEY": "test-access", "QINIU_SECRET_KEY": "test-secret"},
    )
    def test_credentials_enable_official_prefetch_before_get(self):
        events = []
        self.verify.side_effect = lambda *a, **k: (
            events.append("get" if k.get("download_images") else "origin") or True
        )
        self.prefetch.side_effect = lambda *a: events.append("prefetch")
        self.assertTrue(cli.warm_images(self.args, self.repo, self.tools))
        self.assertEqual(events, ["origin", "prefetch", "get"])

    @mock.patch.dict("os.environ", {"QINIU_ACCESS_KEY": "test-access"})
    def test_partial_credentials_fail_without_network(self):
        with self.assertRaises(ValueError):
            cli.warm_images(self.args, self.repo, self.tools)
        self.verify.assert_not_called()


if __name__ == "__main__":
    unittest.main()
