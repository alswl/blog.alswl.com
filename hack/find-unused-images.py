#!/usr/bin/env python3
"""
查找 static/images 目录下未被 content 引用的图片。

用法:
    python3 hack/find-unused-images.py

排除目录在 EXCLUDE_DIRS 中配置，路径相对于 static/images，支持通配符如 2022*。
"""
from __future__ import annotations

import fnmatch
import re
import sys
from pathlib import Path

# 路径配置
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
IMAGES_DIR = ROOT_DIR / "static" / "images"
CONTENT_DIR = ROOT_DIR / "content"

# 排除的目录（相对于 static/images，支持通配符）
EXCLUDE_DIRS = [
    "upload_dropbox",
    "2009",
    "2010",
    "2011",
    "2012",
    "2014",
    "201502",
    "201503",
    "201504",
    "2022*",
    "2023*",
]

IMAGE_EXTENSIONS = frozenset({".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"})
IMAGE_REF_PATTERN = re.compile(r"images/([^)]+)")


def _is_excluded(rel_path: str) -> bool:
    """检查路径是否在排除列表中。"""
    for pattern in EXCLUDE_DIRS:
        if not pattern:
            continue
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(rel_path, f"{pattern}/*"):
            return True
    return False


def _collect_content_refs() -> set[str]:
    """从 content 目录收集所有图片引用（含 basename）。"""
    refs: set[str] = set()
    for path in CONTENT_DIR.rglob("*"):
        if path.suffix not in (".md", ".html"):
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for match in IMAGE_REF_PATTERN.findall(content):
            ref = match.split("?")[0].strip()
            if ref:
                refs.add(ref)
                refs.add(Path(ref).name)
    return refs


def _collect_images() -> list[str]:
    """收集 static/images 下所有图片的相对路径。"""
    images: list[str] = []
    for path in IMAGES_DIR.rglob("*"):
        if path.name == ".DS_Store":
            continue
        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        rel = path.relative_to(IMAGES_DIR).as_posix()
        images.append(rel)
    return sorted(images)


def main() -> int:
    """主入口，返回退出码。"""
    refs = _collect_content_refs()
    all_images = _collect_images()
    scanned = [p for p in all_images if not _is_excluded(p)]

    unused = [
        f"{IMAGES_DIR.relative_to(ROOT_DIR).as_posix()}/{p}"
        for p in scanned
        if p not in refs and Path(p).name not in refs
    ]

    print("扫描 static/images 目录...\n")
    print(f"=== 未被 content 引用的图片 ({len(unused)} / {len(scanned)}) ===\n")
    if unused:
        print("\n".join(sorted(unused)))
        return 1
    print("(无)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
