#!/usr/bin/env bash

grep -lE '\!\[.*\]\(http' -R content/posts
