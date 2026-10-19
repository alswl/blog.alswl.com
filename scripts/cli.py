"""One command surface for authors, Git hooks, and CI."""

from __future__ import annotations

import argparse
import csv
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import quote

from . import banners, images, publishing
from .git import ZERO, Repository
from .runtime import Tools, imagemagick

ROOT = Path(__file__).resolve().parents[1]

HELP = """Log4D 写作工具

环境
  make init-theme                  初始化主题 submodule
  make install-hooks               安装 Git hooks（需要 lefthook）
  make doctor                      检查已安装工具，显示实际版本
  依赖安装命令见 docs/dev/README.md

日常写作
  make new name=YYYY-MM-DD-slug.md   新建草稿
  make serve                       预览文章和草稿
  make enrich post=content/posts/…  补充链接卡片图片与描述（可选联网操作）
  make format-markdown             格式化本次修改的 Markdown
  make resize-images               将本次修改的图片缩到 1000×1000 以内
  make check-content               检查本次内容格式、远端图片、尺寸及全量无用图片
  make build-site                  生产构建至 public/

检查后照常 git add / git commit / git push。工具不会自动暂存内容。

维护
  make sync-images                 同步图片到对象存储
  make warm-images base=<发布前提交> 发布后请求本次 CDN 图片，触发未命中回源
  make verify base=<发布前提交>      验收本次文章与 CDN 图片，失败后重试
  make test                        工具链回归测试
  make audit-content               全量历史报告（预期存在历史问题）
  make clean                       清理构建产物

详细说明：docs/guide/writing.md、docs/dev/README.md
高级参数：python3 -m scripts --help
"""


def markdown(files: list[str]) -> list[str]:
    return [name for name in files if Path(name).suffix.lower() == ".md"]


def raster(files: list[str]) -> list[str]:
    return [
        name
        for name in files
        if name.startswith("static/images/")
        and Path(name).suffix.lower() in images.RASTER
    ]


def image_urls(files: list[str], base_url: str) -> list[str]:
    return list(
        base_url.rstrip("/")
        + "/"
        + quote(name.removeprefix("static/images/"), safe="/")
        for name in files
        if name.startswith("static/images/")
        and Path(name).suffix.lower() in images.EXTENSIONS
    )


def warm_images(args, repo: Repository, tools: Tools) -> bool:
    base = args.base if args.base is not None else os.environ.get("CHANGED_FILES_BASE")
    files = repo.files("push", base=base)
    config = publishing.settings(repo.root)
    urls = image_urls(files, config["cdn_url"])
    if not urls:
        print("本次没有新增或修改的图片，跳过 CDN 回源请求。")
        return True
    access = os.environ.get("QINIU_ACCESS_KEY", "")
    secret = os.environ.get("QINIU_SECRET_KEY", "")
    if bool(access) != bool(secret):
        raise ValueError("QINIU_ACCESS_KEY 与 QINIU_SECRET_KEY 必须成对配置。")
    origin = publishing.site_url(repo.root, tools.resolve("hugo"))
    print("等待发布后的站点图片就绪，再请求 CDN，避免提前缓存 404。", flush=True)
    if not publishing.verify(
        image_urls(files, origin + "/images"), args.attempts, args.interval
    ):
        return False
    if access and secret:
        publishing.prefetch_qiniu(urls, access, secret)
    else:
        print(
            "未配置七牛密钥；使用完整 GET 请求触发缓存未命中回源，已有缓存命中时不会强制刷新。",
            flush=True,
        )
    return publishing.verify(urls, args.attempts, args.interval, download_images=True)


def format_files(
    root: Path, files: list[str], tools: Tools, write: bool = False
) -> bool:
    selected = markdown(files)
    if not selected:
        print("没有需要处理的 Markdown。")
        return True
    command = [
        tools.resolve("prettier"),
        "--write" if write else "--check",
        "--config",
        str(root / ".prettierrc"),
        "--",
        *selected,
    ]
    result = subprocess.run(command, cwd=root, check=False)
    if result.returncode and not write:
        print(
            "格式不合规：运行 make format-markdown，检查后重新暂存。",
            file=sys.stderr,
        )
    return result.returncode == 0


def check_files(root: Path, files: list[str], tools: Tools, full: bool) -> bool:
    files = [
        name
        for name in files
        if (root / name).is_file() and not (root / name).is_symlink()
    ]
    print(
        f"检查 {len(files)} 个文件；无用图片{'全量检查' if full else '跳过（快速检查）'}。",
        flush=True,
    )
    errors: list[str] = []
    valid_format = format_files(root, files, tools)
    content = [name for name in files if Path(name).suffix.lower() in {".md", ".html"}]
    errors.extend(images.remote_images(root, content))
    errors.extend(images.image_sizes(root, raster(files)))
    if full:
        errors.extend(images.unused_images(root))
    for error in errors:
        print(error, file=sys.stderr)
    if valid_format and not errors:
        print("检查通过。")
        return True
    return False


def check(args, repo: Repository, tools: Tools) -> bool:
    base = args.base if args.base is not None else os.environ.get("CHANGED_FILES_BASE")
    files = repo.files(args.scope, base=base)
    if args.scope == "staged":
        selected = files + [".prettierrc"] if args.changed_only else None
        with repo.snapshot(paths=selected) as snapshot:
            return check_files(snapshot, files, tools, not args.changed_only)
    if args.scope == "push":
        with repo.snapshot(ref="HEAD") as snapshot:
            return check_files(snapshot, files, tools, not args.changed_only)
    return check_files(repo.root, files, tools, not args.changed_only)


def hook(kind: str, repo: Repository, tools: Tools) -> bool:
    if kind == "pre-commit":
        added = repo.names("diff", "--cached", "--name-only", "--diff-filter=A", "-z")
        try:
            allow = (
                repo.git("config", "--get", "hooks.allownonascii").strip() == b"true"
            )
        except subprocess.CalledProcessError:
            allow = False
        if not allow and any(not name.isascii() for name in added):
            raise ValueError(
                "新增文件名含非 ASCII 字符；请重命名，或显式设置 git config hooks.allownonascii true。"
            )
        return check(
            argparse.Namespace(scope="staged", base=None, changed_only=True),
            repo,
            tools,
        )
    valid = True
    for line in sys.stdin:
        local_ref, local_sha, remote_ref, remote_sha = line.split()
        if (
            local_sha == ZERO
            or not local_ref.startswith("refs/heads/")
            or remote_ref == "refs/heads/gh-pages"
        ):
            continue
        print(f"检查推送: {local_ref} -> {remote_ref}", flush=True)
        base = remote_sha
        files = repo.files("push", base=base, head=local_sha)
        with repo.snapshot(ref=local_sha) as snapshot:
            valid = check_files(snapshot, files, tools, full=True) and valid
    return valid


def doctor(root: Path, tools: Tools) -> bool:
    valid = True
    print(f"Python {sys.version.split()[0]} ({sys.executable})")
    for name in ("hugo", "prettier"):
        try:
            binary = tools.resolve(name)
            output = subprocess.run(
                [binary, "version" if name == "hugo" else "--version"],
                capture_output=True,
                text=True,
                check=True,
            )
            print(f"OK {name}: {output.stdout.strip()} ({binary})")
        except ValueError as error:
            print(f"缺失: {error}")
            valid = False
    try:
        identify, _ = imagemagick()
        print(f"OK ImageMagick: {identify[0]}")
    except ValueError as error:
        print(f"缺失: {error}")
        valid = False
    if not (root / "themes/hugo-PaperMod/layouts").is_dir():
        print("缺失: 主题 submodule；运行 make init-theme。")
        valid = False
    for name in ("lefthook", "aws"):
        print(f"可选 {name}: {shutil.which(name) or '未安装'}")
    return valid


def build(args, repo: Repository, tools: Tools) -> None:
    if args.cdn and not os.environ.get("CI"):
        raise ValueError(
            "CDN 发布构建只在 CI 运行；本地使用 make build-site 或 make serve。"
        )
    target = repo.root / (".cache/publish" if args.cdn else "public")
    cache = repo.root / ".cache"
    cache.mkdir(exist_ok=True)
    config = publishing.settings(repo.root)
    hugo = tools.resolve("hugo")
    config["site_url"] = publishing.site_url(repo.root, hugo)
    with tempfile.TemporaryDirectory(prefix="build-", dir=cache) as directory:
        output = Path(directory) / "site"
        subprocess.run(
            [hugo, "--environment", "production", "--destination", str(output)],
            cwd=repo.root,
            check=True,
        )
        if args.cdn:
            count = publishing.cdn_artifacts(output, config)
            print(f"CDN 地址已写入 {count} 个发布产物。")
        if target.is_symlink():
            raise ValueError(f"构建目录不能是符号链接: {target}")
        # Replace a nonempty directory only after Hugo succeeds; discard stale assets.
        if target.exists():
            shutil.rmtree(target)
        output.replace(target)
    print(f"构建完成: {target.relative_to(repo.root)}")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Log4D 写作工具；日常入口为 make help。"
    )
    commands = result.add_subparsers(dest="command", required=True)
    commands.add_parser("help", help="显示作者常用命令")
    for name, help_text in (
        ("doctor", "诊断依赖，不修改环境"),
        ("serve", "用已安装的 Hugo 预览草稿"),
        ("format-markdown", "格式化本次 Markdown，不自动暂存"),
        ("resize-images", "缩放工作区图片，不自动暂存"),
        ("clean", "清理构建产物"),
        ("test", "运行工具链回归测试"),
    ):
        commands.add_parser(name, help=help_text)
    p = commands.add_parser(
        "check-content", help="只读门禁，默认检查工作区修改并全量检查无用图片"
    )
    p.add_argument(
        "--scope", choices=("worktree", "staged", "push", "all"), default="worktree"
    )
    p.add_argument("--base", help="push 范围的远端提交；CI 也可传 CHANGED_FILES_BASE")
    p.add_argument("--changed-only", action="store_true", help="跳过全量无用图片检查")
    p = commands.add_parser("build-site", help="生产构建至 public/，成功后替换旧产物")
    p.set_defaults(cdn=False)
    p = commands.add_parser(
        "build-publication", help="CI 专用：构建至 .cache/publish 并转换 CDN 地址"
    )
    p.set_defaults(cdn=True)
    p = commands.add_parser("new", help="新建草稿")
    p.add_argument(
        "name",
        nargs="?",
        default=os.environ.get("BLOG_POST_NAME") or f"{date.today()}-new.md",
    )
    p = commands.add_parser("enrich", help="补充链接卡片图片和描述")
    p.add_argument("files", nargs="*")
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--retry-missing", action="store_true")
    p = commands.add_parser("sync-images", help="显式同步图片到对象存储")
    p.add_argument("--dry-run", action="store_true")
    p = commands.add_parser(
        "warm-images", help="发布后请求本次 CDN 图片，支持可选的七牛官方预热"
    )
    p.add_argument("--base")
    p.add_argument("--attempts", type=int, default=4)
    p.add_argument("--interval", type=float, default=15)
    p = commands.add_parser(
        "verify", help="验收文章 URL 和本次修改的 CDN 图片，记录时间并重试"
    )
    p.add_argument("urls", nargs="*")
    p.add_argument("--scope", choices=("worktree", "push"), default="push")
    p.add_argument("--base")
    p.add_argument("--attempts", type=int, default=4)
    p.add_argument("--interval", type=float, default=15)
    p = commands.add_parser("hook", help="Git 内部调用")
    p.add_argument("kind", choices=("pre-commit", "pre-push"))
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    repo = Repository(ROOT)
    tools = Tools(ROOT)
    try:
        command = args.command
        if command == "help":
            print(HELP)
        elif command == "doctor":
            return 0 if doctor(ROOT, tools) else 1
        elif command == "check-content":
            return 0 if check(args, repo, tools) else 1
        elif command == "hook":
            return 0 if hook(args.kind, repo, tools) else 1
        elif command == "format-markdown":
            return (
                0
                if format_files(ROOT, repo.files("worktree"), tools, write=True)
                else 1
            )
        elif command == "resize-images":
            images.resize(ROOT, raster(repo.files("worktree")))
        elif command == "serve":
            subprocess.run([tools.resolve("hugo"), "serve", "-D"], cwd=ROOT, check=True)
        elif command in {"build-site", "build-publication"}:
            build(args, repo, tools)
        elif command == "new":
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*\.md", args.name):
                raise ValueError(
                    "文件名使用 YYYY-MM-DD-slug.md，slug 仅限英文小写、数字和短横线。"
                )
            subprocess.run(
                [tools.resolve("hugo"), "new", f"posts/{args.name}"],
                cwd=ROOT,
                check=True,
            )
        elif command == "enrich":
            files = args.files or (
                [os.environ["BLOG_POST"]] if os.environ.get("BLOG_POST") else []
            )
            if not files:
                raise ValueError(
                    "请指定文章：make enrich post=content/posts/YYYY-MM-DD-slug.md"
                )
            flags = (["--refresh"] if args.refresh else []) + (
                ["--retry-missing"] if args.retry_missing else []
            )
            return banners.main([*flags, *files])
        elif command == "sync-images":
            config = publishing.settings(ROOT)
            if not shutil.which("aws"):
                raise ValueError("图片同步需要 AWS CLI 和已配置的对象存储凭据。")
            subprocess.run(
                [
                    "aws",
                    "s3",
                    "sync",
                    "--endpoint-url",
                    config["s3_endpoint"],
                    "--exclude",
                    ".*",
                    "--exclude",
                    "*/.*",
                    *(["--dryrun"] if args.dry_run else []),
                    str(ROOT / "static/images"),
                    f"s3://{config['s3_bucket']}/",
                ],
                check=True,
            )
        elif command == "warm-images":
            if args.attempts < 1 or args.interval < 0:
                raise ValueError("attempts 至少为 1，interval 不能为负数。")
            return 0 if warm_images(args, repo, tools) else 1
        elif command == "verify":
            if args.attempts < 1 or args.interval < 0:
                raise ValueError("attempts 至少为 1，interval 不能为负数。")
            config = publishing.settings(ROOT)
            config["site_url"] = publishing.site_url(ROOT, tools.resolve("hugo"))
            base = (
                args.base
                if args.base is not None
                else os.environ.get("CHANGED_FILES_BASE")
            )
            files = repo.files(args.scope, base=base)
            urls = list(args.urls)
            if os.environ.get("BLOG_VERIFY_URL"):
                urls.append(os.environ["BLOG_VERIFY_URL"])
            output = subprocess.run(
                [
                    tools.resolve("hugo"),
                    "list",
                    "published",
                    "--environment",
                    "production",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
            urls += [
                row["permalink"]
                for row in csv.DictReader(io.StringIO(output.stdout))
                if row["path"] in files
            ]
            urls += image_urls(files, config["cdn_url"])
            if not urls:
                urls = [config["site_url"] + "/"]
            return 0 if publishing.verify(urls, args.attempts, args.interval) else 1
        elif command == "clean":
            for relative in ("public", ".cache/publish"):
                path = ROOT / relative
                if path.is_symlink():
                    path.unlink()
                elif path.exists():
                    shutil.rmtree(path)
            (ROOT / ".hugo_build.lock").unlink(missing_ok=True)
        elif command == "test":
            return subprocess.run(
                [
                    sys.executable,
                    "-B",
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "tests",
                    "-v",
                ],
                cwd=ROOT,
                check=False,
            ).returncode
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"错误: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130
