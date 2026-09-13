#!/usr/bin/env bash
#
# Markdown 格式化 / 格式检查。
#
# 用法:
#   hack/format.sh                  # 格式化暂存区的 md 并重新 git add（pre-commit）
#   hack/format.sh a.md b.md        # 格式化指定文件
#   hack/format.sh --check a.md     # 只检查不写入，不合格返回 1
#
# 版本钉在 .prettier-version、规则钉在 .prettierrc，否则上游发版会重排全部文章。

set -uo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
PRETTIER="prettier@$(cat "$ROOT_DIR/.prettier-version")"

check_mode=0
if [ "${1:-}" = "--check" ]; then
    check_mode=1
    shift
fi

check_non_ascii_filenames() {
    [ "$(git config hooks.allownonascii)" = "true" ] && return 0
    git rev-parse --verify HEAD >/dev/null 2>&1 &&
        against=HEAD ||
        against=4b825dc642cb6eb9a060e54bf8d69288fbee4904

    # wc -c 在 macOS 上会输出前导空格，必须去掉再比较
    local bad
    bad=$(git diff --cached --name-only --diff-filter=A -z "$against" |
        LC_ALL=C tr -d '[ -~]\0' | wc -c | tr -d '[:space:]')
    if [ "$bad" != "0" ]; then
        echo "错误: 试图添加非 ASCII 文件名。" >&2
        echo "跨平台协作时这会带来问题，请重命名文件。" >&2
        echo "确实需要时可以: git config hooks.allownonascii true" >&2
        return 1
    fi
}

from_staging=0
md_files=()
if [ $# -gt 0 ]; then
    for arg in "$@"; do
        case "$arg" in
        *.md) [ -f "$arg" ] && md_files+=("$arg") ;;
        esac
    done
else
    from_staging=1
    while IFS= read -r f; do
        [ -n "$f" ] && [ -f "$f" ] && md_files+=("$f")
    done < <(git diff --cached --name-only --diff-filter=ACMR | grep '\.md$')
fi

# 必须在参数分支之外执行：lefthook 总是带 {staged_files} 调用，放进分支里就永远跑不到
if [ "$check_mode" -eq 0 ]; then
    check_non_ascii_filenames || exit 1
fi

if [ ${#md_files[@]} -eq 0 ]; then
    echo "没有需要处理的 Markdown 文件"
    exit 0
fi

if [ "$check_mode" -eq 1 ]; then
    if ! npx --yes "$PRETTIER" --check "${md_files[@]}"; then
        echo >&2
        echo "上述文件格式不合规，运行 make format 修复。" >&2
        exit 1
    fi
    exit 0
fi

npx --yes "$PRETTIER" --write "${md_files[@]}" || exit 1

if [ "$from_staging" -eq 1 ]; then
    git add -- "${md_files[@]}"
else
    for f in "${md_files[@]}"; do
        if git diff --cached --name-only | grep -qx "$f"; then
            git add -- "$f"
        fi
    done
fi
