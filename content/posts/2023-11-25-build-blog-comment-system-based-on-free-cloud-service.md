---
title: "如何免费用云服务搭建博客评论系统"
slug: "build-blog-comment-system-based-on-free-cloud-service"
date: 2023-11-25T17:23:35+08:00
categories: [""]
tags: [""]
draft: true
typora-copy-images-to: ../../static/images/202311
---

# 如何免费用云服务搭建博客评论系统

## 问题

博客自 2012 年从 WordPress 迁移到静态站点后，就选择了 Disqus 作为评论系统。
但最近 Disqus 硬广告过于频繁，迫切<mark>寻找新的评论系统</mark>。

[Disqus 官方](https://help.disqus.com/en/articles/1717119-ads-faq) 明确说明，要去掉广告就付费。

> What if I want to remove Ads?
> If you'd like to remove Disqus Ads from your integration, you may purchase and ads-free subscription from your Subscription and Billing page. More information on Disqus ads-free subscriptions may be found here.

OK，那再见吧 Disqus，我会找到可靠、免费、易用的评论系统。
最后既然是寻找新的评论系统，现在 2023 年了，
我希望这个新系统<mark>充分使用云服务的便利</mark>，要做到
<mark>免费、可靠、易运维</mark>。

![no-disqus-twitter](../../static/images/202311/no-disqus-twitter.png)

## 选型原则

在进入探索之前，我先梳理一下自己的原则和选型要求：

- 数据自有是核心要求
  - 确保评论数据完全归属于博主，不会因为使用第三方服务而失去对数据的控制。
- 服务部署和存储是难点
  - 考虑到服务的稳定性和成本，选择一个易于部署且存储成本较低的方案。
- 访问速度是考虑项
  - 评论系统的访问速度直接关系到用户体验，
    因此需要选择一个能够提供较快访问速度的系统。

从功能上面分析需要的能力：

- 邮件通知
- Markdown
- 内容安全：No Injection
- 评论审核和删除
- 授权登录（Optional）

非功能需求：

- 低成本：控制在 12 元 / 年
- 系统稳定

通过明晰这些原则和要求，可以更有针对性地选择合适的评论系统，确保满足核心功能和非功能需求。接下来，将根据这些原则，继续探讨如何选择和搭建评论系统。

## 初步方案探索

现在我们初步试验一些方案并进行一些探索，以方便我们熟悉一下当前常见系统的<mark>特性和水准</mark>。

### [utterances](https://utteranc.es/)

![utterances](../../static/images/202311/utterances.png)

- 经常见到的一个评论系统，流行于程序员群体，基于 Github Issues 系统因此免费，需要使用 Github 账号登录
- 7.8k star
- 托管在 Github Issues

### [Twikoo](https://twikoo.js.org/quick-start.html)

![twikoo](../../static/images/202311/twikoo.png)

- 国产方案，基于云服务展开，需要寻找云函数部署环境（大部分收费）
- 880 star

### [Cusdis](https://cusdis.com/)

![cusdis](../../static/images/202311/cusdis.png)

- 国产方案，提供免费的 Cloud 服务（但是额度比较受限）
- 2.4k star
- 支持迁移
- 手工通过评论
- 活跃度不高

我同时还看了一些外部的一些方案评测报告：

- [Comments | Hugo](https://gohugo.io/content-management/comments/)
- [静态博客评论系统的选择 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2196035?areaSource=&traceId=)
- [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway） - 少数派](https://sspai.com/post/73412)

根据初步方案探索，我可以明确部署形态基本如下：

![comment-system-deploy-diagram](../../static/images/202311/comment-system-deploy-diagram.png)

## 横向对比

这是一个横向对比表格，列举我一些关心的特性以及候选者在这些特性方面的表现。除了上述提到几款常见软件，
我还额外调研了<mark>海外常用的评论 SaaS 服务</mark>：

| Name            | self-host | Official SaaS | SaaS Free   | Star | Import Disqus | export data | Comments                                   |
| --------------- | --------- | ------------- | ----------- | ---- | ------------- | ----------- | ------------------------------------------ |
| Utterances      | x         | v             | v           | 7.8k |               | v           | Github account required                    |
| Cusdis          | v         | v             | v?          | 2.3k | v             | v?          | import from Disqus failed                  |
| Cactus Comments | v         | v             |             | 100  |               |             | Matrix Protocol, blocked                   |
| Commento        | x         | v             | $10/month   |      | v             | v           |                                            |
| Graph Comment   |           | v             | Free to $7  |      |               |             |                                            |
| Hyvor Talk      | x         | v             | $12/month   |      |               |             |                                            |
| IntenseDebate   |           | v             | ?           |      | x             |             | too old                                    |
| Isso            | v         | x             |             | 4.8k | v             |             | sqlite storage                             |
| Mutt            |           | v             | $16/month   |      |               |             |                                            |
| Remark42        | v         | x             |             | 4.3k | v             | v           | full featured, one file storage            |
| ReplyBox        |           | v             | $5/month    |      |               |             |                                            |
| Staticman       | v         |               |             | 2.3k |               | v           | using github as storage                    |
| Talkyard        |           | v             | €4.5/ month |      |               |             |                                            |
| Waline          | v         |               |             | 1.5k | v             | v           | Multi Storage / Service Provider supported |
| Twikoo          | v         | x             |             | 1.1k | v             | v           | FaaS / MongoDB                             |

根据横向对比我们可以得出几个结论：

- 海外传统评论系统数据透明度低，风格也是是古早型系统
- 官方提供 SaaS 服务普遍需要收费
- self-host 的几个产品需要自己搭建服务，没有一键使用免费的 Cloud Provider 路径

**小结**

符合我需求的几款产品是：Utterances、Cusdis、Waline。

## PoC 和实施

我最后选择了 utterances 和 Waline 进行 PoC，
其中我的[英文博客](https://en.blog.alswl.com/)使用了 utterances，
[中文博客](https://blog.alswl.com/)使用了 Waline。

为什么不选择 Cusdis 和 Twikoo？因为 Cusdis 使用 PostgreSQL，
而 Twikoo 存储使用腾讯云函数（免费额度有限）或者 MongoDB，
存储上 Waline 选择更多。
另外，作为同类型方案，Waline 是三者贡献者数量最多的，Commit 数量也最多，
社区更有保障。

### Waline 实施

> 一个搞笑的点，如果这里使用 h3 标题叫做「Waline」，会直接在这里插入一个当前博客的评论框

- 优点
  - 多平台部署
  - 多数据库支持（MongoDB、sqlite、PostgreSQL、MySQL）
  - 评论功能强大
  - 导入工具
  - 活跃度尚可
- 缺点
  - 功能太多，不够克制（好在可以自定义配置）
  - 国产产品
- 接入流程：
  - 找个 Storage 供应商（我选择 <mark>LeanCloud</mark>）
  - 找个 Server 供应商部署（我选择 <mark>Vercel</mark>）
  - 找个邮件发送供应商（我选择了 <mark>Brevo</mark>（原来叫 SendinBlue））
  - 前端部署（Hugo 内集成一下）

部署图：

![waline](../../static/images/202311/waline.png)

具体操作，跟随官方文档即可：

- [快速上手 | Waline](https://waline.js.org/guide/get-started/)
- [Vercel 部署 | Waline](https://waline.js.org/guide/deploy/vercel.html#%E5%A6%82%0E4%BD%95%E9%83%A8%E7%BD%B2)
- 绑定 CName
- 导入数据
  - 转换 [数据迁移助手 | Waline](https://waline.js.org/migration/tool.html)
  - 导入 https://console.leancloud.app/apps/yours/storage/import-export
- 配置页面
  - 参考配置系统禁用一些评论功能 https://waline.js.org/reference/client/props.html
  - 启用 SMTP
    - 配置 `AUTHOR_EMAIL`
    - 配置 `SENDER_NAME`
    - 配置 `SENDER_EMAIL`
  - 服务端配置 https://waline.js.org/reference/server/config.html#tgtemplate
- 遇到的问题
  - Disqus 导出的用户数据没有邮箱，导致 gravatar 没有照片显示，无解
  - 邮箱配置需要额外配置环境变量，否则会暴露自己的个人邮箱

实施 PR（仅包含前端，因为后端代码包含了密钥，不便于分享）：
[feat: comments on waline · alswl/blog.alswl.com@e34e348](https://github.com/alswl/blog.alswl.com/commit/e34e34810298fd0d716d4c4a467fada25b3a6622)

## Utterances 实施

utterances 的部署则更为简单，一个 PR 就可以启用。
[feat: comment using utteranc · alswl/en.blog.alswl.com@29028f6 (github.com)](https://github.com/alswl/en.blog.alswl.com/commit/29028f677e362570a8bcaf5316847ddfa3e9d685)

也没有什么特色，主打简单省事，考虑我英文博客访问量极低，就简单方案。

## 小结

最后我选择了 Waline / utterances 作为我的评论系统，两者的部署成本都是 0。

妥协牺牲了一些访问速度、安全性，但进一步增强了数据可控性，完成了 self-host。
从稳定性上面来看，尽管这个系统链路变复杂了，单机上也存在可用性风险，
但依托 Vercel / LeanCloud / Brevo 三家 SaaS 服务商，整体风险可控。

毕竟只是一个小小评论系统，0 成本 + 正常工作就行了。

欢迎在下面评测测试一下哦~
