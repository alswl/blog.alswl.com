

前段时间在将公司的 SVN 项目迁移到 Git 上面去，遇到一个很少见的问题：
有一个小伙伴使用 git-svn 做 `rename` 操作时候，将一个目录 `svn mv` 了，
导致新目录只存了最近几个月提交历史，丢失了历史信息。对团队开发而言，
历史提交是非常宝贵的财产，我们想了一些办法，把这些数据提取出来。

<!-- more -->

```
# 找出丢失之前的版本，列出丢失目录上层的操作记录。
svn log -l 2000 svn://log4d.com/trunk/apps/ios/ | less

# 将重命名之前的版本拷贝到一个临时目录
svn copy svn://log4d.com/trunk/apps/ios/nami@43252 svn://log4d.com/trunk/apps/ios/nami_lost

# 准备现有代码到 Git
git svn clone svn://log4d.com/ -T trunk/apps/ios/nami -t tags -b branches -r 13532 nami

# 修改 .git/config 来加入丢失的历史数据 Remote
[svn-remote "svn-lost"]
	url = svn://log4d.com
	fetch = trunk/apps/ios/nami_lost:refs/remotes/trunk-lost

# 并抓取 Remote 内容
git svn fetch

# Rebase 新代码到恢复过来的历史记录上
git checkout master
git rebase --committer-date-is-author-date trunk-lost
```

其中注意的是手动添加一个 `svn-remote` 地址为历史数据副本地址。
还有就是 `rebase` 时候参数 `--committer-date-is-author-date`
可以保证 `rebase` 不会造成提交时间被修改，方便回溯。

整整搞了一天，说出来都是泪，希望看到的人用不到，搜到的人用得到。

