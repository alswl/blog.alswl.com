#!/usr/bin/env bash
#
# 输出本次改动涉及的文件（仓库相对路径，每行一个，只保留仍存在的文件）。
#
# 供 lefthook 的 pre-push 与 CI 共用，是所有「增量检查」的输入来源。
# 仓库里有大量历史存量（384 篇未格式化的文章、76 张超规格图片），
# 全量门禁会立刻失败，所以检查一律只作用于本次改动。
#
# 比较基准（base）的确定顺序：
#   1. 第一个参数（显式指定）
#   2. $CHANGED_FILES_BASE（CI 传入 github.event.before）
#   3. origin/master（本地 pre-push 的常规场景）
#   4. HEAD~1（首次推送 / 浅历史兜底）
# 都不可用时（如仓库只有一个提交）退化为「全部文件」。
#
# 输出 = 相对 base 的提交改动 ∪ 工作区未提交改动（暂存 + 未暂存 + 未跟踪），
# 这样在写作过程中直接跑 `make check-changed` 也能覆盖还没提交的内容。

set -uo pipefail

ZERO=0000000000000000000000000000000000000000

# 若给定的 ref 存在且不是全零 SHA，则打印它并返回 0
resolve_base() {
    local candidate="${1:-}"
    [ -n "$candidate" ] || return 1
    [ "$candidate" != "$ZERO" ] || return 1
    git rev-parse --verify --quiet "${candidate}^{commit}" >/dev/null 2>&1 || return 1
    printf '%s' "$candidate"
}

base=""
for candidate in "${1:-}" "${CHANGED_FILES_BASE:-}" "origin/master" "HEAD~1"; do
    if base=$(resolve_base "$candidate"); then
        break
    fi
    base=""
done

{
    if [ -n "$base" ]; then
        # 三点：从 base 与 HEAD 的共同祖先算起，force push 时也安全
        git diff --name-only --diff-filter=ACMR "${base}...HEAD"
    else
        git ls-files
    fi

    # 工作区里尚未提交的改动
    git diff --name-only --diff-filter=ACMR HEAD 2>/dev/null
    git ls-files --others --exclude-standard
} | sort -u | while IFS= read -r f; do
    # 排除符号链接：CLAUDE.md -> AGENTS.md 这类，prettier 会直接报错，
    # 而且链接目标本身已经在列表里了
    [ -n "$f" ] && [ -f "$f" ] && [ ! -L "$f" ] && printf '%s\n' "$f"
done
