#!/usr/bin/env bash
#
# 输出本次改动涉及的文件（仓库相对路径，每行一个，只保留仍存在的文件）。
# lefthook 的 pre-push 与 CI 共用它，作为所有增量检查的输入。
#
# base 依次取：参数 / $CHANGED_FILES_BASE / origin/master / HEAD~1。
# CI 传入的是 github.event.before，新分支首次推送时它是全零 SHA，必须跳过。
#
# 输出并入了工作区未提交的改动，所以写作途中直接跑 make check-changed 也有效。

set -uo pipefail

ZERO=0000000000000000000000000000000000000000

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

    git diff --name-only --diff-filter=ACMR HEAD 2>/dev/null
    git ls-files --others --exclude-standard
} | sort -u | while IFS= read -r f; do
    # 排除符号链接（CLAUDE.md -> AGENTS.md）：prettier 对符号链接直接报错
    [ -n "$f" ] && [ -f "$f" ] && [ ! -L "$f" ] && printf '%s\n' "$f"
done
