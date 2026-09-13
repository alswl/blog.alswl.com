#!/usr/bin/env bash
#
# 把工作区里新增/修改的图片缩到 1000x1000 以内。
#
# 旧版用 `git status | awk '{print $3}'` 取路径，只有 "new file:   path" 这一种
# 行形态的 $3 才是路径；未 add 的新图（最常见的写作流）和被替换的旧图
# 的 $3 都是空，会被静默跳过。现改用 --porcelain -z 解析，
# 覆盖 未跟踪 / 已修改 / 已暂存 / 重命名 四种状态。

set -uo pipefail

MAX=1000

if ! command -v magick >/dev/null 2>&1; then
    echo "错误: 找不到 magick（ImageMagick 7）" >&2
    exit 1
fi

# --porcelain -z 的记录格式为 "XY <path>\0"，重命名额外多一个 "<origpath>\0"。
# 用 NUL 分隔，文件名含空格也安全。
count=0
while IFS= read -r -d '' entry; do
    status=${entry:0:2}
    path=${entry:3}

    # 重命名/复制记录后面紧跟一个原路径字段，读掉丢弃
    case "$status" in
    R* | C*) IFS= read -r -d '' _orig ;;
    esac

    # 删除的文件没什么好缩的
    case "$status" in
    *D | D*) continue ;;
    esac

    # 只处理 static/images/ 下的图片
    # （旧版的 `grep images` 会误伤任何路径里带 "images" 的文件）
    case "$path" in
    static/images/*) ;;
    *) continue ;;
    esac

    case "$path" in
    *.png | *.jpg | *.jpeg | *.gif | *.webp | *.PNG | *.JPG | *.JPEG) ;;
    *) continue ;;
    esac

    [ -f "$path" ] || continue

    echo "resize $path"
    magick "$path" -strip -auto-orient -resize "${MAX}x${MAX}>" "$path"
    count=$((count + 1))
done < <(git status --porcelain -z)

echo "已处理 $count 张图片"
