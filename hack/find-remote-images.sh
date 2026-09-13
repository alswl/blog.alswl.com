#!/usr/bin/env bash
#
# 检查 markdown 里是否有指向远端 http(s) 的图片引用。
#
# 图片应当落在 static/images/YYYYMM/ 并用 /images/... 绝对路径引用，
# 远端引用会随对方站点失效而烂掉。
#
# 用法:
#   hack/find-remote-images.sh              # 扫描整个 content/
#   hack/find-remote-images.sh a.md b.md    # 只扫描指定文件
#
# 命中返回 1。历史文章尚有存量远端引用，因此日常只对本次改动的文件调用。

set -uo pipefail

# markdown 图片 ![alt](http...) 与 HTML <img src="http...">
PATTERN='!\[[^]]*\]\(https?://|<img[^>]+src="https?://'

files=()
if [ $# -gt 0 ]; then
    for f in "$@"; do
        case "$f" in
        *.md | *.html) [ -f "$f" ] && files+=("$f") ;;
        esac
    done
else
    while IFS= read -r f; do
        files+=("$f")
    done < <(find content -type f \( -name '*.md' -o -name '*.html' \))
fi

[ ${#files[@]} -eq 0 ] && exit 0

hits=$(grep -nEH "$PATTERN" "${files[@]}" 2>/dev/null)

if [ -z "$hits" ]; then
    echo "OK: 没有指向远端的图片引用"
    exit 0
fi

echo "发现指向远端的图片引用：" >&2
echo "$hits" >&2
echo >&2
echo "请把图片下载到 static/images/YYYYMM/ 并改用 /images/YYYYMM/name.png 引用。" >&2
exit 1
