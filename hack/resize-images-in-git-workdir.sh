#!/usr/bin/env sh

for i in $(git status | grep images | awk '{print $3}'); do
    echo resize "$i";
    convert "$i" -resize 1000x1000\> "$i";
done
