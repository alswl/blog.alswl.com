#!/usr/bin/env bash
#
# 检查图片尺寸是否超过 1000x1000。
#
# 用法:
#   hack/check-image-size.sh a.png b.jpg    # 检查指定文件
#   hack/check-image-size.sh                # 检查 static/images 全部（存量有 76 张超标）
#
# 超标返回 1。日常只对本次改动的图片调用（见 hack/changed-files.sh），
# 修复方式是 make resize-images-in-git-workdir。

set -uo pipefail

MAX=1000

# ImageMagick 7 是 `magick identify`，6 是 `identify`
if command -v magick >/dev/null 2>&1; then
    identify_cmd() { magick identify "$@"; }
elif command -v identify >/dev/null 2>&1; then
    identify_cmd() { identify "$@"; }
else
    echo "错误: 找不到 ImageMagick（magick 或 identify）" >&2
    exit 1
fi

files=()
if [ $# -gt 0 ]; then
    for f in "$@"; do
        case "$f" in
        *.png | *.jpg | *.jpeg | *.gif | *.webp | *.PNG | *.JPG | *.JPEG)
            [ -f "$f" ] && files+=("$f")
            ;;
        esac
    done
else
    while IFS= read -r f; do
        files+=("$f")
    done < <(find static/images -type f \
        \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' -o -name '*.gif' -o -name '*.webp' \))
fi

[ ${#files[@]} -eq 0 ] && exit 0

oversized=""
for f in "${files[@]}"; do
    # gif 等多帧格式每帧一行，取第一帧即可
    dim=$(identify_cmd -format '%w %h\n' "$f" 2>/dev/null | head -1)
    [ -n "$dim" ] || continue
    w=${dim% *}
    h=${dim#* }
    if [ "$w" -gt "$MAX" ] || [ "$h" -gt "$MAX" ]; then
        oversized="${oversized}  ${f} (${w}x${h})"$'\n'
    fi
done

if [ -z "$oversized" ]; then
    echo "OK: ${#files[@]} 张图片均在 ${MAX}x${MAX} 以内"
    exit 0
fi

echo "以下图片超过 ${MAX}x${MAX}：" >&2
printf '%s' "$oversized" >&2
echo "请运行: make resize-images-in-git-workdir" >&2
exit 1
