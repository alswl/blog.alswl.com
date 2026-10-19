"""Build-artifact URL conversion and publication verification."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def settings(root: Path) -> dict[str, str]:
    values = json.loads((root / "scripts/publishing.json").read_text())
    for name in ("cdn_url", "s3_endpoint"):
        if not values.get(name, "").startswith("https://"):
            raise ValueError(f"scripts/publishing.json: {name} 必须为 HTTPS URL。")
        values[name] = values[name].rstrip("/")
    if not values.get("s3_bucket"):
        raise ValueError("scripts/publishing.json 缺少 s3_bucket。")
    return values


def site_url(root: Path, hugo: str) -> str:
    output = subprocess.run(
        [hugo, "config", "--environment", "production", "--format", "json"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    # Ask Hugo to resolve its own configuration; do not duplicate baseURL or parse YAML.
    return json.loads(output.stdout)["baseurl"].rstrip("/")


def rewrite_cdn(source: str, site: str, cdn: str) -> str:
    # Keep escaping, whitespace, and code outside URL tokens intact. This handles
    # HTML, feed entities, Markdown links/references, and !banner image markers.
    boundary = r"""(?P<before>["'(<]|&(?:quot|apos|#34|#39|lt);|\]:[ \t]+)"""
    pattern = boundary + r"(?:" + re.escape(site.rstrip("/")) + r")?/images/"
    result = re.sub(pattern, lambda m: m["before"] + cdn.rstrip("/") + "/", source)

    def srcset(match):
        value = re.sub(
            r"(?<![^,\s])(?:" + re.escape(site.rstrip("/")) + r")?/images/",
            cdn.rstrip("/") + "/",
            match[2],
        )
        return match[1] + value + match[3]

    return re.sub(r"""(srcset=["'])(.*?)(["'])""", srcset, result, flags=re.DOTALL)


def cdn_artifacts(directory: Path, config: dict[str, str]) -> int:
    changed = 0
    # Search JSON and feeds embed images too; binary assets must remain byte-identical.
    for path in directory.rglob("*"):
        if (
            path.suffix.lower() not in {".html", ".xml", ".md", ".json"}
            or not path.is_file()
        ):
            continue
        source = path.read_text(encoding="utf-8")
        updated = rewrite_cdn(source, config["site_url"], config["cdn_url"])
        if updated != source:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def prefetch_qiniu(urls: list[str], access_key: str, secret_key: str) -> None:
    """Submit official CDN prefetch jobs; acceptance is not task completion."""
    if not access_key or not secret_key:
        raise ValueError(
            "七牛官方预热需要同时配置 QINIU_ACCESS_KEY 和 QINIU_SECRET_KEY。"
        )
    path = "/v2/tune/prefetch"
    # QBox signs the path and newline; application/json bodies are not signed.
    signature = base64.urlsafe_b64encode(
        hmac.new(secret_key.encode(), (path + "\n").encode(), hashlib.sha1).digest()
    ).decode()
    selected = list(dict.fromkeys(urls))
    for offset in range(0, len(selected), 20):
        batch = selected[offset : offset + 20]
        request = Request(
            "https://fusion.qiniuapi.com" + path,
            data=json.dumps({"urls": batch}).encode(),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"QBox {access_key}:{signature}",
            },
            method="POST",
        )
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
        if (
            result.get("code") != 200
            or result.get("invalidUrls")
            or result.get("error") not in (None, "", "success")
        ):
            raise ValueError(f"七牛预热未受理全部图片: {result}")
        print(
            f"七牛预热已受理 {len(batch)} 张图片，requestId={result.get('requestId', '未提供')}。",
            flush=True,
        )


def verify(
    urls: list[str],
    attempts: int = 4,
    interval: float = 15,
    *,
    download_images: bool = False,
) -> bool:
    pending = dict.fromkeys(urls)
    for attempt in range(attempts):
        for url in list(pending):
            stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
            try:
                with urlopen(
                    Request(
                        url,
                        method="GET" if download_images else "HEAD",
                        headers={"User-Agent": "Log4D publication check"},
                    ),
                    timeout=20,
                ) as response:
                    if response.status != 200:
                        raise ValueError(f"HTTP {response.status}")
                    if download_images:
                        content_type = response.headers.get_content_type()
                        if not content_type.startswith("image/"):
                            raise ValueError(f"响应不是图片: {content_type}")
                        size = 0
                        while chunk := response.read(64 * 1024):
                            size += len(chunk)
                        if not size:
                            raise ValueError("图片响应为空")
                        expected = response.headers.get("Content-Length")
                        if expected is not None and size != int(expected):
                            raise ValueError(f"图片响应不完整: {size}/{expected} 字节")
                print(f"{stamp} OK {url}", flush=True)
                del pending[url]
            except (HTTPError, URLError, OSError, HTTPException, ValueError) as error:
                print(f"{stamp} 等待 {url}: {error}", flush=True)
        if not pending:
            return True
        if attempt + 1 < attempts:
            time.sleep(interval)
    return False
