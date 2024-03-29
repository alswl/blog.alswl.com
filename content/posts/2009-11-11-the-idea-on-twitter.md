---
title: "关于Twitter的idea"
author: "alswl"
slug: "the-idea-on-twitter"
date: "2009-11-11T00:00:00+08:00"
tags: ["关注互联网", "twitter"]
categories: ["internet"]
---

## 起因-同步是个麻烦事

这几天写了几篇博文，想自动同步博文url到各类SNS以及微博，但是发现一下子同步是很麻烦的事情。就我手头维护的话，需要更新Twitter、人人、新浪微博，如
果能同步一个内容就发布到所有网站，这该多好啊。

对了，关于同步，帮[xDash](http://www.fanbing.net/)打一个小广告：他建了一个站点，[同步控](http://www.syncoo.com/)，还是挺不错的。

## 现状-已有先行者

将一个状态发散式同步到其他SNS网站肯定不是我想出来的，已经有很多网站在运营着了。比如…

[嘀神](http://www.digusync.com/)--自动把你的状态同步到人人、开心等所有社交网站！

[HelloTxt](http://hellotxt.com/): 同时更新你的Twitter、饭否和Plurk…

嘀神的问题在于他是基于[嘀咕](http://digu.com)的，在微博这一块，digu并不是最强，虽然推出了**OpenCloud**这个概念，但是似乎
开放API的程度成为诟病，可以看出，所谓**火兔**、**打嘀**、**嘀神**的一堆广播产品都是自家出品。业内曾经指出嘀咕的开放并不是真正的开放（当然，这
是目前中国IT普遍存在的，没有核心技术来保留用户群，只能用这种不开放API的手段）。嘀神能更新的也不多，**Twitter**就不在其中。

HelloTxt被墙了，我没有办法去仔细研究，依稀记得当时HelloTxt居然支持**饭否**，让我很惊讶他的同步群……

虽有先行者，势弱也~

## 我的想法-更多交流

光能扩散式更新还不够，我们要把所有的微博互动起来，省的一句话从Twitter同步到新浪围脖，围脖的人回复了却不知道，人家岂不是对着镜子讲话么（引用[Tim]
(http://xirang.us/)语）。所以我们必须能够跨平台回复、回推，甚至引入新功能（扩散回推）。

现在这个互动已经不仅仅是扩散发布，而应该是真正意义上的互相沟通，这在技术上只要有API的支持就不难实现。（在此鄙视那些伪开放API的SNS）

还有一个重要功能就是消息发布，可以通过RSS协议从**这个站点**获取所有微博的信息，而不用关注每个微博。

这个站点的适用人群是拥有很多微博，朋友分布在各个微博，都不肯统一。那么只能自己统一到这个平台进行处理，而不要奔波于各个网站。

不知道这样的站点现在有没有人实现，我觉得这是很有金的想法，毕竟这么一个平台将会架空Twitter以及其他微博，使自己成为一个**唯一**通行路口。应该可以形
成自己的运营模式。

## 死穴-基本只能玩玩了

想法总是好的，实施起来就比较难了。

在国外，人家盛行Twitter，用不到这个多博客更新，只有在国内才百花齐放（百花齐败？）。而在国内，这种Web2.0自由说话的地方肯定有风险，容易遭来「服务
器休整」。

怎么规避风险？嗯```用GAE开发，然后做成每个人单独的个人系统，就可以简单规避，只不过这样以来，就无法形成商业化的运营了。等我工作定下来，真想花时间在GA
E弄一个，然后作为毕业设计，哈哈。

如果可以，Google在Wave加上这个功能，那么就犀利了，应该可以主导微博市场了。

ps：想想而已，小的目光短浅，见识少，各位嘴下留情啊```

