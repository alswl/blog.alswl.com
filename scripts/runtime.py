"""Pinned build tools, installed explicitly and reused offline."""

from __future__ import annotations

import hashlib
import platform
import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path
from urllib.request import urlopen


class Tools:
    def __init__(self, root: Path, version_root: Path | None = None):
        self.root = root
        self.version_root = version_root or root
        self.cache = root / ".cache" / "tools"

    def version(self, name: str) -> str:
        value = (self.version_root / f".{name}-version").read_text().strip()
        if not re.fullmatch(r"\d+\.\d+\.\d+", value):
            raise ValueError(f".{name}-version 中的版本无效: {value}")
        return value

    def candidate(self, name: str) -> Path:
        folder = self.cache / name / self.version(name)
        return folder / ("hugo" if name == "hugo" else "node_modules/.bin/prettier")

    def resolve(self, name: str) -> str:
        expected = self.version(name)
        choices = [str(self.candidate(name))]
        # Reuse exact system pins so setup does not require redundant downloads.
        if system := shutil.which(name):
            choices.append(system)
        for binary in choices:
            if not Path(binary).is_file():
                continue
            output = subprocess.run(
                [binary, "version" if name == "hugo" else "--version"],
                capture_output=True,
                text=True,
                check=False,
            )
            match = re.search(r"(?:hugo v)?(\d+\.\d+\.\d+)", output.stdout)
            if output.returncode == 0 and match and match.group(1) == expected:
                return binary
        raise ValueError(
            f"缺少指定版本的 {name} {expected}。运行 make setup；不会使用其他版本代替。"
        )

    def setup(self) -> None:
        for name in ("hugo", "prettier"):
            try:
                binary = self.resolve(name)
                print(f"已就绪: {name} {self.version(name)} ({binary})", flush=True)
                continue
            except ValueError:
                pass
            target = self.candidate(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            if name == "hugo":
                self.install_hugo(target)
            else:
                if not shutil.which("npm"):
                    raise ValueError(
                        "缺少 npm；请先安装 Node.js LTS，再运行 make setup。"
                    )
                subprocess.run(
                    [
                        "npm",
                        "install",
                        "--prefix",
                        str(target.parents[2]),
                        "--no-save",
                        "--package-lock=false",
                        "--ignore-scripts",
                        "--no-audit",
                        "--no-fund",
                        f"prettier@{self.version(name)}",
                    ],
                    check=True,
                )
            print(
                f"已安装: {name} {self.version(name)} ({self.resolve(name)})",
                flush=True,
            )

    def install_hugo(self, target: Path) -> None:
        # Empty caches must bootstrap the pin, with checksum validation before replacement.
        version = self.version("hugo")
        system = platform.system().lower()
        machine = platform.machine().lower()
        if system == "darwin":
            architecture = "universal"
        elif system == "linux" and machine in {"x86_64", "amd64", "aarch64", "arm64"}:
            architecture = "amd64" if machine in {"x86_64", "amd64"} else "arm64"
        else:
            raise ValueError(
                "自动安装支持 macOS 和 Linux amd64/arm64；其他平台请安装版本文件指定的 Hugo。"
            )
        archive_name = f"hugo_{version}_{system}-{architecture}.tar.gz"
        base = f"https://github.com/gohugoio/hugo/releases/download/v{version}"
        print(f"下载 Hugo {version} ({system}-{architecture})", flush=True)
        with tempfile.TemporaryDirectory(prefix="blog-hugo-") as directory:
            archive_path = Path(directory) / archive_name
            with (
                urlopen(f"{base}/{archive_name}", timeout=120) as response,
                archive_path.open("wb") as stream,
            ):
                shutil.copyfileobj(response, stream)
            with urlopen(
                f"{base}/hugo_{version}_checksums.txt", timeout=30
            ) as response:
                checksums = response.read().decode()
            expected = next(
                (
                    line.split()[0]
                    for line in checksums.splitlines()
                    if line.split()[-1].lstrip("*") == archive_name
                ),
                None,
            )
            actual = hashlib.sha256(archive_path.read_bytes()).hexdigest()
            if actual != expected:
                raise ValueError("Hugo 下载校验失败；未安装。")
            with (
                tarfile.open(archive_path) as archive,
                archive.extractfile("hugo") as binary,
            ):
                temporary = target.with_suffix(".tmp")
                with temporary.open("wb") as stream:
                    shutil.copyfileobj(binary, stream)
                temporary.chmod(0o755)
                temporary.replace(target)


def imagemagick() -> tuple[list[str], list[str]]:
    if binary := shutil.which("magick"):
        return [binary, "identify"], [binary]
    identify, convert = shutil.which("identify"), shutil.which("convert")
    if identify and convert:
        return [identify], [convert]
    raise ValueError(
        "缺少 ImageMagick：macOS 运行 brew install imagemagick，Ubuntu 安装 imagemagick。"
    )
