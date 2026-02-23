#!/usr/bin/env sh
#
# 查找 static/images 目录下未被 content 引用的图片
# 用法: ./hack/find-unused-images.sh
#
# 排除目录: 在 EXCLUDE_DIRS 中添加，每行一个，路径相对于 static/images
#

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
IMAGES_DIR="$ROOT_DIR/static/images"
CONTENT_DIR="$ROOT_DIR/content"

# 排除的目录列表（相对于 static/images 的路径，每行一个）
EXCLUDE_DIRS="
upload_dropbox
2009
2010
2011
2012
2014
201502
201503
201504
"

# 检查路径是否在排除列表中
is_excluded() {
    local rel_path="$1"
    for dir in $EXCLUDE_DIRS; do
        [ -z "$dir" ] && continue
        case "$rel_path" in
            "$dir"|"$dir"/*) return 0 ;;
        esac
    done
    return 1
}

# 临时文件
content_refs=$(mktemp)
refs_normalized=$(mktemp)
images_list=$(mktemp)
unused_list=$(mktemp)
trap 'rm -f "$content_refs" "$refs_normalized" "$images_list" "$unused_list"' EXIT

# 收集 content 目录下所有文本内容
find "$CONTENT_DIR" -type f \( -name "*.md" -o -name "*.html" \) -exec cat {} \; 2>/dev/null > "$content_refs"

# 从 content 中提取所有图片引用，归一化为 "path/to/image.ext" 格式
# 匹配: static/images/xxx, images/xxx, /images/xxx (到 ) 或行尾)
# 支持带查询参数的引用，如 image.png?1d5d3d
# 同时提取文件名，用于匹配同一图片在不同路径的情况（如 2009/05/email163.gif 与 upload_dropbox/200905/email163.gif）
grep -oE 'images/[^)]+' "$content_refs" 2>/dev/null | \
    sed 's|^images/||; s|\?.*||' | \
    sort -u > "$refs_normalized"
{
    cat "$refs_normalized"
    while IFS= read -r ref; do
        [ -z "$ref" ] && continue
        basename "$ref"
    done < "$refs_normalized"
} | sort -u > "${refs_normalized}.tmp" && mv "${refs_normalized}.tmp" "$refs_normalized"

# 查找所有图片文件（排除 .DS_Store）
find "$IMAGES_DIR" -type f \( \
    -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o \
    -iname "*.gif" -o -iname "*.webp" -o -iname "*.svg" \
\) ! -name ".DS_Store" 2>/dev/null | sort -u > "$images_list"

echo "扫描 static/images 目录..."
echo ""

# 检查每张图片是否在引用列表中（排除 exclude 目录）
while IFS= read -r img_path; do
    [ -z "$img_path" ] && continue
    rel_path="${img_path#$IMAGES_DIR/}"
    rel_path="${rel_path#/}"
    is_excluded "$rel_path" && continue
    img_name=$(basename "$rel_path")

    # 检查完整路径或文件名是否被引用
    grep -qFx "$rel_path" "$refs_normalized" 2>/dev/null && continue
    grep -qFx "$img_name" "$refs_normalized" 2>/dev/null && continue

    echo "${IMAGES_DIR#$ROOT_DIR/}/$rel_path"
done < "$images_list" | sort -u > "$unused_list"

unused_count=$(wc -l < "$unused_list" | tr -d ' ')
# total_count 不含排除目录
total_count=0
while IFS= read -r img_path; do
    [ -z "$img_path" ] && continue
    rel_path="${img_path#$IMAGES_DIR/}"
    rel_path="${rel_path#/}"
    is_excluded "$rel_path" || total_count=$((total_count + 1))
done < "$images_list"

echo "=== 未被 content 引用的图片 ($unused_count / $total_count) ==="
echo ""
if [ "$unused_count" -gt 0 ]; then
    cat "$unused_list"
    exit 1
else
    echo "(无)"
fi
