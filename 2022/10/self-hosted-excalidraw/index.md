

> 首先感谢岳父岳母带家中神兽去过暑假了，我才能有周末的时间来改这个系统。
>
> 另外感谢老婆，周末我两天都搞自己的事情，也没批评我。
>
> 最后感谢公司团建，提供酒店住，花了一个晚上时间搞定了中文手写体。
>
> 注：这是魔改私有化 excalidraw 开源版本，感谢社区


## #1 Excalidraw

> 介绍一下 Excalidraw，产品特性

什么是 Excalidraw，<mark>这（可能）是最强的在线协同画图工具</mark> ，你可以访问 [Excalidraw](https://excalidraw.com/) 试试看。

![anatomy\_of\_an\_azure\_function.png](/images/202210/anatomy_of_an_azure_function.png)

如果你觉得打开来都是空白，那么也可以访问这个公共面板 [Excalidraw](https://excalidraw.com/#room=e630a562422e6e9d94db,IXndkz3JfOSGrlswJRC83Q) 参与一起创作。

![excalidraw-share-room.png](/images/202210/excalidraw-share-room.png)

Excalidraw 非常好用，我总结几个点：

-   手写风格（Hand Writing）避免了强迫症，什么一像素差异，都没了躺平到底
-   无延迟在线协作，非常适合后疫情时代的沟通协作
-   产品素质过硬，快捷键、对象连接粘滞、选定文件直接存储到本地等细节都有，挑不出毛病

![excalidraw-homepage.png](/images/202210/excalidraw-homepage.png)

这个产品我们经内部同学内部安利之后，大家迅速的喜欢上了，在 Excalidraw 上面了好多图，但也引来一个问题。

<center><mark><b>「公有 SaaS 服务存在数据安全隐患」</b></mark></center>

<center><mark><b> 怎么办？我要把他私有化部署！</b></mark></center>

## #2 部署之前，先来了解一下 Excalidraw 的工作原理

**Excalidraw 工作原理和私有化原理**：

![excalidraw-arch.png](/images/202210/excalidraw-arch.png)

那私有化的核心难点是什么：

解决 excalidraw-storage 的数据存储问题，即替换掉 Google Cloud Platform 的 firebase 服务。

## #3 私有化尝试

> 事有不顺反求诸己
>
> \- 孟子
>
> 求与诸己，不如求于 GayHub
>
> \- alswl

让我们先先研究 Excalidraw 的存储系统。
Firebase 是 Google 的 Serverless 服务，以前是独立公司（还挺火），后来给 GCP 收购了。

![firebase.png](/images/202210/firebase.png)

![firebase-features.png](/images/202210/firebase-features.png)

我一开始想法是替换 Firebase，找了一个社区服务 [Supabase](https://supabase.com/)（意外发现还有免费的 SaaS 服务，良心啊）

![supabase.png](/images/202210/supabase.png)

但是仔细研究一下，发现 Supabase 的 API 和 firebase 不兼容，并 <mark>不能平替</mark>。

Excalidraw 还要靠 Excalidraw+ 卖钱（Plus 服务），怎么可能让你这么轻松就私有化，官方原来有个 excalidraw-json 的仓库，现在也被移除了。但是我们不怕，我们有来自社区的力量：

-   [Self hosting Excalidraw - Umbrella issue · Issue #1772 · excalidraw/excalidraw](https://github.com/excalidraw/excalidraw/issues/1772)
-   [Collaboration mode - Self-hosting vs Collab on top of · Discussion #3879 · excalidraw/excalidraw (github.com)](https://github.com/excalidraw/excalidraw/discussions/3879)

他们给了条路（虽然后来被证实还是有歪路的）：

-   [Kilian Decaderincourt / Excalidraw Fork · GitLab](https://gitlab.com/kiliandeca/excalidraw-fork) 魔改版本 excalidraw
-   [Kilian Decaderincourt / excalidraw-storage-backend · GitLab](https://gitlab.com/kiliandeca/excalidraw-storage-backend)

于是我开始检视他们方案，打开代码一看，思路正确（替换 firebase 的几个接口），使用自己的 KV 存储（Redis / MySQL / Mongo）替换。

![jing-shen.png](/images/202210/jing-shen.png)

尝试部署，立马遇到问题：

<center><mark><b> Dockerfile 无法正常构建 </b></mark></center>

<center><mark><b> 版本落后 upstream 太久（2020 -\> 2022）</b></mark></center>

<center><mark><b> Rebase 方式 merge 上游无法 follow </b></mark></center>

怎么这么巧，我是 <mark><b> 前端实习生 // 社区打补丁专家 // Kubernetes 清洁工 // YAML 资深专家 </b></mark>，专治这么几个毛病。

## #4 你让开，我来写


-   [alswl/excalidraw-storage-backend: Excalidraw Backend](https://github.com/alswl/excalidraw-storage-backend)
    -   使用二阶段构建 Dockerfile https://github.com/alswl/excalidraw-storage-backend/commit/d841d734ab02659df370a6bdef3f1d8947696580](https://github.com/alswl/excalidraw-storage-backend/commit/d841d734ab02659df370a6bdef3f1d8947696580)
    -   中国特供 [feat: china mirror · alswl/excalidraw-storage-backend@30a6da9](https://github.com/alswl/excalidraw-storage-backend/commit/30a6da9c87b367bb1fbde449f754923638545fa8)
-   [alswl/excalidraw: Virtual whiteboard for sketching hand-drawn like diagrams](https://github.com/alswl/excalidraw)
    -   调整代码，使用 http stroage 替代 firebase
    -   [Feat/self host backend by alswl · Pull Request #2 · alswl/excalidraw](https://github.com/alswl/excalidraw/pull/2)

<center><mark><b> 改造代码设计图 </b></mark></center>

![self-hosted-excalidraw.png](/images/202210/self-hosted-excalidraw.png)

## #5 未来（可能不存在）

Excalidraw 是 SaaS 服务的免费版，<mark><b> Excalidraw+ 是付费版 </b></mark>，有什么区别呢

![excalidraw-price.png](/images/202210/excalidraw-price.png)

总结：

-   更可靠的存储，集成到云存储（比如 Dropbox / iCloud）
-   用户身份识别，连接到通用的身份系统
-   更个性化的权限控制（密码访问、定向分享）、租户控制、项目组控制
-   域内共享的 Library
-   跟其他系统集成（语雀、钉钉文档、飞书等等）

或者还是直接购买 Excalidraw 企业版本服务吧，少折腾多享受。


## #6 中文手写体优化

有个问题，<mark><b> 中文字体不是手写体 </b></mark> ，很违和。先看看哪些字体能用吧：

macOS 支持的中文手写体：

-   [https://support.apple.com/zh-cn/HT212587](https://support.apple.com/zh-cn/HT212587)
-   [macOS Monterey 附带的字体 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/HT212587)

cursive 家族：

-   PanziPen
-   LingWai
-   Hannotate

![hanzipen-sc.png](/images/202210/hanzipen-sc.png)

windows 中文支持手写体比较差劲，必须安装 Office 才有更多选择：\
华文行楷；方正舒体；（Office）

-   [https://www.zhihu.com/question/22703287](https://www.zhihu.com/question/22703287)
-   [Windows 系统内置的中文字体为什么只有那几种？不多内置几种字体呢？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/22703287)
-   [https://zh.m.wikipedia.org/zh-hans/Microsoft_Windows字型列表](https://zh.m.wikipedia.org/zh-hans/Microsoft_Windows%E5%AD%97%E5%9E%8B%E5%88%97%E8%A1%A8)

不行的话，只有系统自带的楷体 KaiTi 可以工作。

最后，靠我三脚猫的前端水平，做了一个 PoC，并给官方提交了一个 PR：[feat: simple impl of multi font support, for chinese font by alswl · Pull Request #5604 · excalidraw/excalidraw](https://github.com/excalidraw/excalidraw/pull/5604)

这是最终的效果：

![chinese-hand-writing.png](/images/202210/chinese-hand-writing.png)

可以访问 [excalidraw.alswl.com](https://excalidraw.alswl.com/) 查看效果，这是一个静态站点，
支持中文字体，但是无法在线协作。

----

## Update 2022-12

有几个网友来咨询如何进行部署。于是基于上述的方案，我提供了一套基于 Docker Compose 的一键拉起服务：带协作、中文字体支持。
仓库见 [alswl/excalidraw-collaboration](https://github.com/alswl/excalidraw-collaboration)。

