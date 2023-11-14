

![Stack Overflow](/images/upload_dropbox/201709/stack-overflow.jpg)

*   原文作者：Nick Craver
*   翻译作者：[罗晟 @luosheng](https://twitter.com/luosheng) & [@alswl](https://twitter.com/alswl)
*   原文地址：[Nick Craver - HTTPS on Stack Overflow: The End of a Long Road](https://nickcraver.com/blog/2017/05/22/https-on-stack-overflow/)
*   本文为原创翻译文章，已经获得原作者授权，转载请注明作者及出处。
*   本文首发在「沪江技术学院」公众号

----

今天，我们默认在 [Stack Overflow](https://stackoverflow.com/) 上部署了 HTTPS。目前所有的流量都将跳转到 `https://` 上。与此同时，Google 链接也会在接下去的几周内更改。启用的过程本身只是举手之劳，但在此之前我们却花了好几年的时间。到目前为止，HTTPS 在我们所有的 Q&A 网站上都默认启用了。

[在过去的两个月里](https://meta.stackoverflow.com/q/345012/13249)，我们在 Stack Exchange 全网维持发布 HTTPS。Stack Overflow 是最后，也是迄今最大的的一个站点。这对我们来说是一个巨大里程碑，但决不意味着是终点。[后文会提到](#next-steps)，我们仍有很多需要做的事情。但现在我们总算能看得见终点了，耶！

友情提示：这篇文章讲述的是一个漫长的旅程。非常漫长。你可能已经注意到你的滚动条现在非常小。我们遇到的问题并不是只在 Stack Exchange/Overflow 才有，但这些问题的组合还挺罕见。我在文章中会讲到我们的一些尝试、折腾、错误、成功，也会包括一些开源项目——希望这些细节对你们有所帮助。由于它们的关系错综复杂，我难以用时间顺序来组织这篇文章，所以我会将文章拆解成架构、应用层、错误等几个主题。

<!-- more -->

首先，我们要提一下为什么我们的处境相对独特：

-   我们有几百个域名（[大量站点](https://stackexchange.com/sites)及服务）
    -   大量二级域名（[stackoverflow.com](https://stackoverflow.com/)、[stackexchange.com](https://stackexchange.com/)、[askubuntu.com](https://askubuntu.com/)等）
    -   大量四级域名（如 [meta.gaming.stackexchange.com](http://meta.gaming.stackexchange.com/)）
-   我们允许用户提交、嵌入内容（比如帖子中的图片和 YouTube 视频）
-   我们仅有一个数据中心（造成单源的延时）
-   我们有广告（及广告网络）
-   我们用 websockets，任何时刻的活跃数都不少于 50 万个（连接数问题）
-   我们会被 DDoSed 攻击（代理问题）
-   我们有不少站点及应用还是通过 HTTP API 通信的（代理问题）
-   我们热衷于性能（*好像*有点太过了）

由于这篇文章实在太长，我在这里先列出链接：

-   [开篇](#the-beginning)
-   [懒人包](#quick-specs)
-   基础设施
    -   [证书](#certificates)
        -   [Meta 子域（meta.\*.stackexcange.com）](#certificates-child-metas-metastackexchangecom)
    -   [性能：HTTP/2](#performance-http2)
    -   [HAProxy：支持 HTTPS](#haproxy-serving-up-https)
    -   [CDN/代理层：通过 Cloudflar 和 Fastly 优化延迟](#cdnproxy-countering-latency-with-cloudflare--fastly)
        -   [优化代理层的准备：客户端性能测试](#preparing-for-a-proxy-client-timings)
        -   [CloudFlare](#cloudflare)
            -   [Railgun](#cloudflare-railgun)
        -   [Fastly](#fastly)
    -   [全局 DNS](#global-dns)
    -   [测试](#testing)
-   应用层/代码
    -   [应用层准备](#preparing-the-applications)
    -   [全局登录](#global-login)
    -   [本地 HTTPS 开发](#local-https-development)
    -   混合内容
        -   [来自你们](#mixed-content-from-you)
        -   [来自我们](#mixed-content-from-us)
    -   [跳转（301）](#redirects-301s)
    -   [Websockets](#websockets)
-   [未知](#unknowns)
-   [错误](#mistakes)
    -   [相对协议 URL](#mistakes-protocol-relative-urls)
    -   [API 及 .internal](#mistakes-apis-and-internal)
    -   [301 缓存](#mistakes-301-caching)
    -   [帮助中心的小插曲](#mistakes-help-center-snafu)
-   [开源](#open-source)
-   [下一步](#next-steps)
    -   [HSTS 预加载](#hsts-preloading)
    -   [聊天](#chat)
    -   [今天](#today)

### 开篇

我们[早在 2013](https://nickcraver.com/blog/2013/04/23/stackoverflow-com-the-road-to-ssl/) 年就开始考虑在 Stack Overflow 上部署 HTTPS 了。是的，现在是 2017 年。所以，**究竟是什么拖了我们四年？**这个问题的答案放在任何一个 IT 项目上都适用：依赖和优先级。老实说，Stack Overflow 在信息安全性上的要求并不像别家那么高。我们不是银行，也不是医院，我们也不涉及信用卡支付，[甚至于我们每个季度都会通过 HTTP 和 BT 种子的方式发布我们大部分的数据库](https://archive.org/details/stackexchange)。这意味着，从安全的角度来看，这件事情的紧急程度不像它在其他领域里那么高。而从依赖上来说，我们的复杂度比别人要高，在部署 HTTPS 时会在几大领域里踩坑，这些问题的组合是比较特殊的。后文中会看到，有一些域名的问题还是一直存在的。

容易踩坑的几个领域包括：

-   用户内容（用户可以上传图片或者指定 URL）
-   广告网络（合同及支持）
-   单数据中心托管（延迟）
-   不同层级下的[**几百个**域名](https://stackexchange.com/sites)（证书）

那我们究竟是为什么需要 HTTPS 呢？因为数据并不是唯一需要安全性的东西。我们的用户中有操作员、开发者、还有各个级别的公司员工。我们希望他们到我们站点的通信是安全的。我们希望每一个用户的浏览历史是安全的。某些用户暗地里喜欢 monad 却又害怕被人发现。同时，Google 会[提升 HTTPS 站点的搜索排名](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html)（虽然我们不知道能提升多少）。

哦，还有**性能**。我们热爱性能。我热爱性能。你热爱性能。我的狗热爱性能。让我给你一个性能的拥抱。很好。谢谢。你闻起来很香。

### 懒人包

很多人喜欢情人包，所以我们来一场快速问答（我们喜欢问答！）：

-   问：你们支持什么协议？
    -   答：TLS 1.0、1.1、1.2（注意：[Fastly 准备放弃 TLS 1.0 和 1.1](https://www.fastly.com/blog/phase-two-our-tls-10-and-11-deprecation-plan))。我们马上也会支持 TLS 1.3。
-   问：你们支持 SSL v2 或者 v3 吗？
    -   答：不支持。[这些协议不安全](http://disablessl3.com/)。大家都应该尽早禁用。
-   问：你们支持哪些加密套件？
    -   答：CDN 上，我们用的是 [Fastly 的默认套件](https://www.ssllabs.com/ssltest/analyze.html?d=meta.stackexchange.com&s=151.101.129.69#suitesHeading)；
    -   答：我们自己的负载均衡器上用的是 [Mozilla 的现代兼容性套件](https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility)。
-   问：Fastly 回源走的是 HTTPS 吗？
    -   答：是。如果到 CDN 的请求是 HTTPS，回源的请求也是 HTTPS。
-   问：你们支持前向安全性吗？
    -   答：是。
-   问：你们支持 [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) 吗？
    -   答：支持。我们正在 Q&A 站点中逐步支持。一旦完成的话我们就会将其移至节点上。
-   问：你们支持 HPKP 吗？
    -   答：不支持，应该也不会支持。
-   问：你们支持 SNI 吗？
    -   答：不支持。出于 HTTP/2 性能考虑，我们使用是一个合并的通配符证书（详见后文）。
-   问：你们的证书是哪来的？
    -   答：我们用的是 [DigiCert](https://www.digicert.com/)，他们很棒。
-   问：你们支持 IE 6 吗？
    -   答：这次之后终于不再支持了。IE 6 默认不支持 TLS（尽管你可以启用 1.0 的支持），而我们则不支持 SSL。当我们 301 跳转就绪的时候大部分 IE 6 用户就不能访问 Stack Overflow 了。一旦我们弃用 TLS 1.0，所有 IE 6 用户都不行了。
-   问：你们负载均衡器用的什么？
    -   答：[HAProxy](https://www.haproxy.org/)（内部使用的是 [OpenSSL](https://www.openssl.org/)）。
-   问：使用 HTTPS 的动机是什么？
    -   答：有人一直攻击我们的管员员路由，如 [stackoverflow.com/admin.php](https://stackoverflow.com/admin.php)。

### 证书

让我们先聊聊证书，因为这是最容易被误解的部分。不少朋友跟我说，他安装了 HTTPS 证书，因此他们已经完成 HTTPS 准备了。呵呵，麻烦你看一眼右侧那个小小的滚动条，这篇文章才刚刚开始，你觉得真的这么简单么？[我有这个必要告诉你们一点人生的经验](https://en.wikipedia.org/wiki/Scientific_wild-ass_guess) ：没这么容易的。

一个最常见的问题是：「为何不直接用 [Let’s Encrypt](https://letsencrypt.org/)？」

答案是：这个方案不适合我们。 Let’s Encrypt 的确是一个伟大的产品，我希望他们能够长期服务于大家。当你只有一个或少数几个域名时，它是非常出色的选择。但是很可惜，我们 Stack Exchange 有[数百个站点](https://stackexchange.com/sites)，而 Let’s Encrypt 并[不支持通配域名配置](https://letsencrypt.org/docs/faq/)。这导致 Let’s Encrypt 无法满足我们的需求。要这么做，我们就不得不在每上一个新的 Q&A 站点的时候都部署一个（或两个）证书。这样会增加我们部署的复杂性，并且我们要么放弃不支持 SNI 的客户端（大约占 2% 的流量）要么提供超多的 IP——而我们目前没这么多的 IP。

我们之所以想控制证书，还有另外一个原因是我们想在本地负载均衡器以及 CDN / 代理提供商那边使用完成相同的证书。如果不做到这个，我们无法顺畅地做从代理那里做失效备援（failover）。支持 [HTTP 公钥固定（HPKP）](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning)的客户端会报认证失败。虽然我们仍在评估是否使用 HPKP，但是如果有一天要用的话我们得提前做好准备。

很多朋友在看见我们的主证书时候会吓得目瞪口呆，因为它包含了我们的主域名和通配符子域名。它看上去长成这样：

[![Main Certificate](/images/upload_dropbox/201709/HTTPS-MainCertificate.png)](../../static/images/upload_dropbox/201709/HTTPS-MainCertificate.png)

为什么这么做？老实说，是我们让 [DigiCert](https://www.digicert.com/) 替我们做的。这么做会导致每次发生变化的时候都需要手动合并证书，了　我们为什么要忍受这么麻烦的事呢？首先，我们期望能够尽可能让更多用户使用我们产品。这里面包括了那些还不支持 SNI 的用户（比如在我们项目启动的时候 Android 2.3 势头正猛）。另外，也包括 HTTP/2 与一些现实问题——我们过会儿会谈到这一块。

Meta 子域（meta.\*.[stackexcange.com](http://stackexcange.com/)）

Stack Exchage 的一个设计理念是，针对每个 Q&A 站点，我们都有一个地方供讨论。我们称之为 [“second place”](https://stackoverflow.blog/2010/04/29/do-trilogy-sites-need-a-third-place/)。比如 `meta.gaming.stackexchange.com` 用来讨论 `gaming.stackexchange.com`。这个有什么特别之处呢？好吧，并没有，除了域名：这是一个 4 级域名。

我之前已经说过[这个问题](https://nickcraver.com/blog/2013/04/23/stackoverflow-com-the-road-to-ssl/)，但后来怎么样了呢？具体来说，现在面临的问题是 `*.stackexchange.com` 包含 `gaming.stackexchange.com`（及几百个其它站点），但它**并不包含** `meta.gaming.stackexchange.com`。[RFC 6125 （第 6.4.3 节）](https://tools.ietf.org/html/rfc6125#section-6.4.3) 写道：

> 客户端 **不应该** 尝试匹配一个通配符在中间的域名（比如，不要匹配 `bar.*.example.net`）

这意味着我们无法使用 `meta.*.stackexchange.com`，那怎么办呢？

-   方案一：部署 [SAN 证书（多域名证书）](https://www.digicert.com/subject-alternative-name.htm)
    -   我们需要准备 3 个证书和 3 个 IP（每张证书支持域名上限是 100），并且会把新站上线复杂化（虽然这个机制已经改了）
    -   我们要在 CDN/代理层上部署三个自定义证书
    -   我们要给 `meta.*` 这种形式的域名配置额外的 DNS 词条
        -   根据 DNS 规则，我们必须给每个这样的站点配置一条 DNS，无法批量配置，从而提高了新站上线和维护代理的成本
-   方案二：将所有域名迁移到 `*.meta.stackexchange.com`
    -   我们会有一次痛苦的迁移过程，但这是一次性的，并且未来维护证书成本较低
    -   我们需要部署一个全局登录系统（[详情见此](#global-login)）
    -   这个方案仍然不解决 HSTS 预加载下面的 `includeSubDomains` 问题（[详情见此](#hsts-reloading)）
-   方案三：啥都不做，放弃
    -   这个方案最简单，然而这是假方案

我们部署了 [全局登录系统](#global-login)，然后将子 meta 域名用 301 重定向到新地址，比如 [gaming.meta.stackexchange.com](https://gaming.meta.stackexchange.com)。做完这个之后我们才意识到，因为这些域名*曾经*存在过，所以对于 HSTS 预加载来说是个很大的问题。这件事情还在进行中，我会在[文章最后面](#hsts-preloading)讨论这个问题。这类问题对于 `meta.pt.stackoverflow.com` 等站点也存在，不过还好我们只有四个非英语版本的 Stack Overflow，所以问题没有被扩大。

对了，这个方案本身还存在*另一个*问题。由于将 cookies 移动到顶级目录，然后依赖于子域名对其的继承，我们必须调整一些其他域名。比如，在我们新系统中，我们使用 SendGrid 来发送邮件（进行中）。我们从 `stackoverflow.email` 这个域名发邮件，邮件内容里的链接域名是 `sg-links.stackoverflow.email`（使用 [CNAME](https://en.wikipedia.org/wiki/CNAME_record) 管理)，这样你的浏览器就不会将敏感的 cookie 发出去。如果这个域名是 `links.stackoverflow.com`，那么你的浏览器会将你在这个域名下的 cookie 发送出去。 我们有不少虽然使用我们的域名，但并不属于我们自己的服务。这些子域名都需要从我们受信的域名下移走，否则我们就会把你们的 cookie 发给非我们自有的服务器上。如果因为这种错误而导致 cookie 数据泄露，这将是件很丢人的事情。

我们有试过通过代理的方式来访问我们的 Hubspot CRM 网站，在传输过程中可以将 cookies 移除掉。但是很不幸 Hubspot 使用 [Akamai](https://www.akamai.com/)，它会判定我们的 HAProxy 实例是机器人，并将其封掉。头三次的时候还挺有意思的……当然这也说明这个方式真的不管用。我们后来再也没试过了。

你是否好奇为什么 Stack Overflow 的博客地址是  <https://stackoverflow.blog/>？没错，这也是出于安全目的。我们把博客搭在一个外部服务上，这样市场部门和其他团队能够更便利地使用。正因为这样，我们不能把它放在有 cookie 的域名下面。

上面的方案会牵涉到子域名，引出 [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) [预加载](https://hstspreload.org/) 和 `includeSubDomains` 命令问题，我们一会来谈这块内容。

### 性能：HTTP/2

很久之前，大家都认为 HTTPS 更慢。在那时候也确实是这样。但是时代在变化，我们说 HTTPS 的时候不再是单纯的 HTTPS，而是基于 HTTPS 的 HTTP/2。虽然 [HTTP/2 不要求加密](https://http2.github.io/faq/#does-http2-require-encryption)，但*事实上*却是加密的。主流浏览器都要求 HTTP/2 提供加密连接来启用其大部分特性。你可以来说 spec 或者规定上不是这么说的，但浏览器才是你要面对的现实。我诚挚地期望这个协议直接改名叫做 HTTPS/2，这样也能给大家省点时间。各浏览器厂商，你们听见了吗？

HTTP/2 有很多功能上的增强，特别是在用户请求之前可以主动推送资源这点。这里我就不展开了，[Ilya Grigorik 已经写了一篇非常不错的文章](https://hpbn.co/http2/)。我这里简单罗列一下主要优点：

-   [请求/响应多路复用](https://hpbn.co/http2/#request-and-response-multiplexing)
-   [服务端推送](https://hpbn.co/http2/#server-push)
-   [Header 压缩](https://hpbn.co/http2/#header-compression)
-   [网络流优先级](https://hpbn.co/http2/#stream-prioritization)
-   [更少的连接](https://hpbn.co/http2/#one-connection-per-origin)

咦？怎么没提到证书呢？

一个很少人知道的特性是，[你可以推送内容到不同的域名](https://hpbn.co/optimizing-application-delivery/#eliminate-domain-sharding)，只要满足以下的条件：

1.  这两个域名需要解析到同一个 IP 上
2.  这两个域名需要使用同一张 TLS 证书（看到没！）

让我们看一下我们当前 DNS 配置：

```
λ dig stackoverflow.com +noall +answer
; <<>> DiG 9.10.2-P3 <<>> stackoverflow.com +noall +answer
;; global options: +cmd
stackoverflow.com.      201     IN      A       151.101.1.69
stackoverflow.com.      201     IN      A       151.101.65.69
stackoverflow.com.      201     IN      A       151.101.129.69
stackoverflow.com.      201     IN      A       151.101.193.69

λ dig cdn.sstatic.net +noall +answer
; <<>> DiG 9.10.2-P3 <<>> cdn.sstatic.net +noall +answer
;; global options: +cmd
cdn.sstatic.net.        724     IN      A       151.101.193.69
cdn.sstatic.net.        724     IN      A       151.101.1.69
cdn.sstatic.net.        724     IN      A       151.101.65.69
cdn.sstatic.net.        724     IN      A       151.101.129.69
```

嘿，这些 IP 都是一致的，并且他们也拥有相同的证书！这意味着你可以直接使用 HTTP/2 的服务器推送功能，而无需影响 HTTP/1.1 用户。 HTTP/2 有推送的同时，HTTP/1.1 也有了[域名共享](https://blog.stackpath.com/glossary/domain-sharding/)（通过 `sstatic.net`）。我们暂未部署服务器推送功能，但一切都尽在掌握之中。

HTTPS 是我们实现性能目标的一个手段。可以这么说，我们的主要目标是性能，而非站点安全性。我们想要安全性，但光是安全性不足以让我们花那么多精力来在全网部署 HTTPS。当我们把所有因素都考虑在一起的时候，我们可以评估出要完成这件事情需要付出的巨大的时间和精力。在 2013 年，HTTP/2 还没有扮演那么重要的角色。而现在形势变了，对其的支持也多了，最终这成为了我们花时间调研 HTTPS 的催化剂。

值得注意的是 HTTP/2 标准在我们项目进展时还在持续发生变化。它从 [SPDY](https://en.wikipedia.org/wiki/SPDY) 演化为 [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)，从 [NPN](https://tools.ietf.org/id/draft-agl-tls-nextprotoneg-03.html) 演化为 [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation)。我们这里不会过多涉及到这部分细节，因为我们并没有为其做太多贡献。我们观望并从中获准，但整个互联网却在推进其向前发展。如果你感兴趣，可以看看 [Cloudflare 是怎么讲述其演变的](https://blog.cloudflare.com/introducing-http2/)。

### HAProxy：支持 HTTPS

我们最早在 2013 年开始在 HAProxy 中使用 HTTPS。为什么是 [HAProxy](https://www.haproxy.org/) 呢？这是历史原因，我们已经在使用它了，而它在 2013 年 的 [1.5 开发版](https://www.haproxy.org/news.html)中支持了 HTTPS，并在 2014 年发布了正式版。曾经有段时间，我们把 Nginx 放置在 HAProxy 之前（[详情看这里](https://nickcraver.com/blog/2013/04/23/stackoverflow-com-the-road-to-ssl/)）。但是简单些总是更好，我们总是想着要避免在链路、部署和其他问题上的复杂问题。

我不会探讨太多细节，因为也没什么好说的。HAProxy 在 1.5 之后使用 OpenSSL 支持 HTTPS，配置文件也是清晰易懂的。我们的配置方式如下：

-   跑在 4 个进程上
    -   1 个用来做 HTTP/前端处理
    -   2-4 个用来处理 HTTPS 通讯
-   HTTPS 前端使用 [socket 抽象命名空间](https://unix.stackexchange.com/a/206395/400)来连接至 HTTP 后端，这样可以极大减少资源消耗
-   每一个前端或者每一「层」都监听了 :433 端口（我们有主、二级、websockets 及开发环境）
-   当请求进来的时候，我们在请求头上加入一些数据（也会移除掉一些你们发送过来的），再将其转发给 web 层
-   我们使用  [Mozilla 提供的加密套件](https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility)。注意，这和我们 CDN 用的不是同样的套件。

HAProxy 比较简单，这是我们使用一个 SSL 证书来支持 :433 端口的第一步。事后看来，这也只是一小步。

这里是上面描述情况下的架构图，我们马上来说前面的那块云是怎么回事：

[![Logical Architecture](/images/upload_dropbox/201709/HTTPS-Layout.svg)](../../static/images/upload_dropbox/201709/HTTPS-Layout.svg)

### CDN/代理层：通过 Cloudflare 和 Fastly 优化延迟

我对 Stack Overflow [架构](https://nickcraver.com/blog/2016/02/17/stack-overflow-the-architecture-2016-edition/)[的效率](https://stackexchange.com/performance)一直很自豪。我们很厉害吧？仅用一个数据中心和几个服务器就撑起了一个大型网站。不过这次不一样了。尽管效率这件事情很好，但是在延迟上就成了个问题。我们不需要那么多服务器，我们也不需要多地扩展（不过我们有一个灾备节点）。这一次，这就成为了问题。由于光速，我们（暂时）无法解决延迟这个基础性问题。我们听说有人已经在处理这个问题了，不过他们造的时间机器好像有点问题。

让我们用数字来理解延迟。赤道长度是 40000 公里（光绕地球一圈的最坏情况）。[光速](https://en.wikipedia.org/wiki/Speed_of_light)在真空中是 299,792,458 米/秒。很多人用这个数字，但光纤并不是真空的。实际上光纤有 [30-31% 损耗](https://physics.stackexchange.com/q/80043/653)，所以我们的这个数字是：(40,075,000 m) / (299,792,458 m/s \* .70) = 0.191s，也就是说最坏情况下绕地球一圈是 191ms，对吧？不对。这假设的是一条理想路径，而实际上两个网络节点的之间几乎不可能是直线。中间还有路由器、交换机、缓存、处理器队列等各种各样的延迟。累加起来的延迟相当可观。

这些和 Stack Overflow 有什么关系呢？云主机的优势出来了。如果你用一家云供应商，你访问到的就是相对较近的服务器。但对我们来说不是这样，你离服务部署在纽约或丹佛（主备模式）越远，延迟就越高。而使用 HTTPS，在协商连接的时候需要一个额外的往返。这还是最好的情况（[使用 0-RTT 优化 TLS 1.3](https://blog.cloudflare.com/introducing-0-rtt/)）。[Ilya Grigorik](https://twitter.com/igrigorik) 的 [这个总结](https://istlsfastyet.com/) 讲的很好。

来说 [Cloudflare](https://www.cloudflare.com/) 和 [Fastly](https://www.fastly.com/)。HTTPS 并不是闭门造车的一个项目，你看下去就会知道，我们还有好几个项目在并行。在搭建一个靠近用户的 HTTPS 终端（以降低往返时间）时，我们主要考虑的是：

-   终端 HTTPS 支持
-   DDoS 防护
-   CDN 功能
-   与直连等同或更优的性能

### 优化代理层的准备：客户端性能测试

开始正式启用终端链路加速之前，我们需要有性能测试报告。我们在浏览器搭好了一整套覆盖全链路性能数据的测试。 浏览器里可以通过 JavaScript 从 [`window.performance`](https://www.w3.org/TR/navigation-timing/) 取性能耗时。打开你浏览器的审查器，你可以亲手试一下。我们希望这个过程透明，所以从第一天开始就把详细信息[放在了 teststackoverflow.com](https://teststackoverflow.com/) 上。这上面并没有敏感信息，只有一些由页面*直接*载入的 URI 和资源，以及它们的耗时。每一张记录下来的页面大概长这样：

[![teststackoverflow.com](/images/upload_dropbox/201709/HTTPS-Teststackoverflow.png)](../../static/images/upload_dropbox/201709/HTTPS-Teststackoverflow.png)

我们目前对 5% 的流量做性能监控。这个过程没有那么复杂，但是我们需要做的事情包括：
1. 把耗时转成 JSON
2. 页面加载后上传性能测试数据
3. 将性能测试上传给我们后台服务器
4. 在 SQL Server 中使用 [clustered columnstore](http://www.nikoport.com/columnstore/) 存储数据
5. 使用 [Bosun](https://bosun.org/) (具体是 [BosunReporter.NET](https://github.com/bretcope/BosunReporter.NET)) 汇集数据

最终的结果是我们有了一份来自于全球*真实*用户的很好的实时汇总。这些数据可供我们分析、监控、报警，以及用于评估变化。它大概长这样：

[![Client Timings Dashboard](/images/upload_dropbox/201709/HTTPS-ClientTimings.png)](../../static/images/upload_dropbox/201709/HTTPS-ClientTimings.png)

幸好，我们有持续的流量来获取数据以供我们决策使用，目前的量级是 50 亿，并且还在增长中。这些数据概览如下：

[![Client Timings Database](/images/upload_dropbox/201709/HTTPS-ClientTimingsDatabase.png)](../../static/images/upload_dropbox/201709/HTTPS-ClientTimingsDatabase.png)

OK，我们已经把基础工作准备好了，是时候来测试 CDN/代理层供应商了。

### Cloudflare

我们评估了很多 CDN/DDoS 防护层供应商。最终选择了 [Cloudflare](https://www.cloudflare.com/)，主要是考虑到他们的基础设施、快速响应、还有他们承诺的 [Railgun](https://www.cloudflare.com/website-optimization/railgun/)。那么我们如何测试使用了 Cloudfalre 之后用户的真实效果？是否需要部署服务来获取用户数据？答案是不需要！

Stack Overflow 的数据量非常大：月 PV 过十亿。记得我们上面讲的客户端耗时纪录吗？我们每天都有几百万的访问了，所以不是直接可以问他们吗？我们是可以这么做，只需要在页面中嵌入 `<iframe>` 就行了。Cloudflare 已经是我们 [cdn.sstatic.net](https://cdn.sstatic.net/)（我们共用的无 cookie 的静态内容域）的托管商了。但是这是通过一条[`CNAME` DNS 纪录](https://en.wikipedia.org/wiki/CNAME_record)来做的，我们把 DNS 指向他们的 DNS。所以要用 Cloudflare 来当代理服务的话，我们需要他们指向我们的 DNS。所以我们先需要测试他们 DNS 的性能。

实际上，要测试性能我们需要把二级域名给他们，而不是 `something.stackoverflow.com`，因为这样可能会有不一致的[胶水记录](https://wiki.gandi.net/en/glossary/glue-record)而导致多次查询。明确一下，[一级域名 (TLDs)](https://en.wikipedia.org/wiki/Top-level_domain)指的是 `.com`, `.net`, `.org`, `.dance`, `.duck`, `.fail`, `.gripe`, `.here`, `.horse`, `.ing`, `.kim`, `.lol`, `.ninja`, `.pink`, `.red`, `.vodka`. 和 `.wtf`。 注意，[这些域名尾缀都是](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains)，我可没开玩笑。 [二级域名 (SLDs)](https://en.wikipedia.org/wiki/Second-level_domain) 就多了一级，比如 `stackoverflow.com`, `superuser.com` 等等。我们需要测的就是这些域名的行为及表现。因此，我们就有了 `teststackoverflow.com`，通过这个新域名，我们在全球范围内测试 DNS 性能。对一部分比例的用户，通过嵌一个 `<iframe>`（在测试中开关），我们可以轻松地获取用户访问 DNS 的相关数据。

注意，测试过程最少需要 24 小时。在各个时区，互联网的表现会随着用户作息或者 Netflix 的使用情况等发生变化。所以要测试一个国家，需要完整的一天数据。最好是在工作日（而不要半天落在周六）。我们知道会有各种意外情况。互联网的性能并不是稳定的，我们要通过数据来证明这一点。

我们最初的假设是，多增加了的一个节点会带来额外的延时，我们会因此损失一部分页面加载性能。但是 DNS 性能上的增加其实弥补了这一块。比起我们只有一个数据中心来说，Cloudflare 的 DNS 服务器部署在离用户更近的地方，这一块性能要好得多得多。我希望我们能有空来放出这一块的数据，只不过这一块需要很多处理（以及托管），而我现在也没有足够多的时间。

接下来，我们开始将 `teststackoverflow.com` 放在 Cloudflare 的代理上做链路加速，同样也是放在 `<iframe>` 中。我们发现美国和加拿大的服务由于多余的节点而变慢，但是世界其他地方都是持平或者更好。这满足我们的期望。我们开始使用 Cloudflare 的网络对接我们的服务。期间发生了一些 DDos 的攻击，不过这是另外的事了。那么，为什么我们接受在美国和加拿大地区慢一点呢？因为每个页面加载需要的时间仅为 200-300ms，哪怕慢一点也还是飞快。当时我们认为 [Railgun](https://www.cloudflare.com/website-optimization/railgun/) 可以将这些损耗弥补回来。

这些测试完成之后，我们为了预防 DDos 工作，做了一些其他工作。我们接入了额外的 ISP 服务商以供我们的 CDN/代理层对接。毕竟如果能绕过攻击的话，我们没必要在代理层做防护。现在每个机房都有 4 个 ISP 服务商（译者注：相当于电信、联通、移动、教育网），两组路由器，他们之间使用 [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol)协议。我们还额外添置了两组负载均衡器专门用于处理 CDN/代理层的流量。

Cloudflare: Railgun

与此配套，我们启用了两组 [Railgun](https://www.cloudflare.com/website-optimization/railgun/)。Railgun 的原理是在 Cloudflare 那边，使用 [memcached](https://memcached.org/) 匹配 URL 进行缓存数据。当 Railgun 启用的时候，每个页面（有一个大小阈值）都会被缓存下来。那么在下一次请求时候，如果在这个 URL 在 Cloudflare 节点上和我们这里都缓存的话，我们仍然会问 web 服务器最新的数据。但是我们不需要传输完整的数据，只需要把传输和上次请求的差异数据传给 Cloudflure。他们把这个差异运用于他们的缓存上，然后再发回给客户端。这时候， [gzip 压缩](https://en.wikipedia.org/wiki/Gzip) 的操作也从 Stack Overflow 的 9 台 Web Server 转移到了一个 Railgun 服务上，这台服务器得是 CPU 密集型的——我指出这点是因为，这项服务需要评估、购买，并且部署在我们这边。

举个例子，想象一下，两个用户打开同一个问题的页面。从浏览效果来看，他们的页面技术上长得*几乎*一样，仅仅有细微的差别。如果我们大部分的传输内容只是一个 diff 的话，这将是一个巨大的性能提升。

总而言之，Railgun 通过减少大量数据传输的方式提高性能。当它顺利工作的时候确实是这样。除此之外，还有一个额外的优点：请求不会重置连接。由于 [TCP 慢启动](https://en.wikipedia.org/wiki/TCP_congestion_control#Slow_start)，当连接环境较为复杂时候，可能导致连接被限流。而 Railgun 始终以固定的连接数连接到 Cloudflare 的终端，对用户请求采用了多路复用，从而其不会受慢启动影响。小的 diff 也减少了慢启动的开销。

很可惜，我们由于种种原因我们在使用 Railgun 过程中一直遇到问题。据我所知，我们拥有当时最大的 Railgun 部署规模，这把 Railgun 逼到了极限。尽管我们花了一年追踪各种问题，最终还是不得不放弃了。这种状况不仅没有给我们省钱，还耗费了更多的精力。现在几年过去了。如果你正在评估使用 Railgun，你最好看最新的版本，他们一直在做[优化](https://www.cloudflare.com/docs/railgun/changelog.html)。我也建议你自己做决定是否使用 Railgun。

### Fastly

我们最近才迁到 [Fastly](https://www.fastly.com/)，因为我们在讲 CDN/代理层，我也会顺带一提。由于很多技术工作在 Cloudflare 那边已经完成，所以迁移本身并没有什么值得说的。大家会更感兴趣的是：为什么迁移？毕竟 Cloudflare 在各方面是不错的：丰富的数据中心、稳定的带宽价格、包含 DNS 服务。答案是：它不再是我们最佳的选择了。Flastly 提供了一些我们更为看中的特性：灵活的终端节点控制能力、配置快速分发、自动配置分发。并不是说 Cloudflare 不行，只是它不再适合 Stack Overflow 了。

事实胜于雄辩：如果我不认可 Cloudflare，我的私人博客不可能选择它，嘿，就是这个博客，你现在正在阅读的。

Fastly 吸引我们的主要功能是提供了 [Varnish](https://en.wikipedia.org/wiki/Varnish_(software)) 和 [VCL](https://docs.fastly.com/guides/vcl/)。这提供了高度的终端可定制性。有些功能吧，Cloudfalre 无法快速提供（因为他们是通用化的，会影响所有用户），在 Fastly 我们可以自己做。这是这两家架构上的差异，这种「代码级别高可配置」对于我们很适用。同时，我们也很喜欢他们在沟通、基础设施的开放性。

我来展示一个 VCL 好用在哪里的例子。最近我们遇到 .NET 4.6.2 的一个[超恶心 bug](https://github.com/Microsoft/dotnet/issues/330)，它会导致 max-age 有超过 2000 年的缓存时间。快速解决方法是在终端节点上有需要的时候去覆盖掉这个头部，当我写这篇文章的时候，这个 VCL 配置是这样的：

```nginx
sub vcl_fetch {
  if (beresp.http.Cache-Control) {
      if (req.url.path ~ "^/users/flair/") {
          set beresp.http.Cache-Control = "public, max-age=180";
      } else {
          set beresp.http.Cache-Control = "private";
      }
  }
```

这将给用户能力展示页 3 分钟的缓存时间（数据量还好），其余页面都不设置。这是一个为解决紧急时间的非常便于部署的全局性解决方案。 我们很开心现在有能力在终端做一些事情。我们的 [Jason Harvey](https://twitter.com/alioth) 负责 VCL 配置，并写了一些自动化推送的功能。我们基于一个 Go 的开源库 [fastlyctl](https://github.com/alienth/fastlyctl) 做了开发。

另一个 Fastly 的特点是可以使用我们自己的证书，Cloudflare 虽然也有这个服务，但是费用太高。如我上文提到的，我们现在已经具备使用 HTTP/2 推送的能力。但是，Fastly 就不支持 DNS，这个在 Cloudflare 那里是支持的。现在我们需要自己解决 DNS 的问题了。可能最有意思的就是这些来回的折腾吧？

### 全局 DNS

当我们从 Cloudflare 迁移到 Fastly 时候，我们必须评估并部署一个新的 DNS 供应商。这里有篇 [Mark Henderson](https://twitter.com/thefarseeker) 写的 [文章](http://blog.serverfault.com/2017/01/09/surviving-the-next-dns-attack/) 。鉴于此，我们必须管理：

-   我们自己的 DNS 服务器（备用）
-   [Name.com](http://name.com/) 的服务器（为了那些不需要 HTTPS 的跳转服务）
-   Cloudflare DNS
-   Route 53 DNS
-   Google DNS
-   Azure DNS
-   其他一些（测试时候使用）

这个本身就是另一个项目了。为了高效管理，我们开发了 [DNSControl](http://blog.serverfault.com/2017/04/11/introducing-dnscontrol-dns-as-code-has-arrived/)。这现在已经是[开源项目了](https://stackexchange.github.io/dnscontrol/)，[托管在 GiHub](https://github.com/StackExchange/dnscontrol) 上，使用 [Go](https://golang.org/) 语言编写。 简而言之，每当我们推送 JavaScript 的配置到 git，它都会马上在全球范围里面部署好 DNS 配置。这里有一个简单的例子，我们拿 [askubuntu.com](https://askubuntu.com/) 做示范：

```
D('askubuntu.com', REG_NAMECOM,
    DnsProvider(R53,2),
    DnsProvider(GOOGLECLOUD,2),
    SPF,
    TXT('@', 'google-site-verification=PgJFv7ljJQmUa7wupnJgoim3Lx22fbQzyhES7-Q9cv8'), // webmasters
    A('@', ADDRESS24, FASTLY_ON),
    CNAME('www', '@'),
    CNAME('chat', 'chat.stackexchange.com.'),
    A('meta', ADDRESS24, FASTLY_ON),
END)
```

太棒了，接下来我们就可以使用客户端响应测试工具来测试啦！[上面提到的工具](#preparing-for-a-proxy-client-timings)可以实时告诉我们真实部署情况，而不是模拟数据。但是我们还需要测试所有部分都正常。

### 测试

客户端响应测试的追踪可以方便我们做性能测试，但这个并不适合用来做配置测试。客户端响应测试非常适合展现结果，但是配置有时候并没有界面，所以我们开发了 [httpUnit](https://godoc.org/github.com/StackExchange/httpunit) （后来知道[这个项目重名了](http://httpunit.sourceforge.net/) ）。这也是一个使用 Go 语言的[开源项目](https://github.com/StackExchange/httpunit)。以 `teststackoverflow.com` 举例，使用的配置如下：

```ini
[[plan]]
    label = "teststackoverflow_com"
    url = "http://teststackoverflow.com"
    ips = ["28i"]
    text = "<title>Test Stack Overflow Domain</title>"
    tags = ["so"]
[[plan]]
    label = "tls_teststackoverflow_com"
    url = "https://teststackoverflow.com"
    ips = ["28"]
    text = "<title>Test Stack Overflow Domain</title>"
    tags = ["so"]
```

每次我们更新一下防火墙、证书、绑定、跳转时都有必要测一下。我们必须保证我们的修改不会影响用户访问（先在预发布环境进行部署）。 httpUnit 就是我们来做集成测试的工具。

我们还有一个开发的内部工具（由亲爱的 [Tom Limoncelli](https://twitter.com/yesthattom) 开发），用来管理我们负载均衡上面的 [VIP 地址](https://en.wikipedia.org/wiki/Virtual_IP_address) 。我们先在一个备用负载均衡上面测试完成，然后将所有流量切过去，让之前的主负载均衡保持一个稳定状态。如果期间发生任何问题，我们可以轻易回滚。如果一切顺利，我们就把这个变更应用到那台负载均衡上。这个工具叫做 `keepctl`（keepalived control 的简称），时间允许的话很快就会整理开源出来。

### 应用层准备

上面提到的只是架构方面的工作。这通常是由 [Stack Overflow 的几名网站可靠性工程师](http://stackoverflow.com/company/team#Engineering)组成的团队完成的。而应用层也有很多需要完成的工作。这个列表会很长，先让我拿点咖啡和零食再慢慢说。

很重要的一点是，[Stack Overflow 与 Stack Exchange 的架构](https://nickcraver.com/blog/2016/02/17/stack-overflow-the-architecture-2016-edition/) Q&A 采用了[多租户技术](https://en.wikipedia.org/wiki/Multitenancy)。这意味着如果你访问 `stackoverflow.com` 或者 `superuser.com` 又或者 `bicycles.stackexchange.com`，你返回到的其实是同一台服务器上的同一个 `w3wp.exe` 进程。我们通过浏览器发送的 [`Host` 请求头](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host)来改变请求的上下文。为了更好地理解我们下文中提到的一些概念，你需要知道我们代码中的 `Current.Site` 其实指的是 *请求* 中的站点。`Current.Site.Url()` 和 `Current.Site.Paths.FaviconUrl` 也是基于同样的概念。

换一句话说：我们的 Q&A 全站都是跑在同一个服务器上的同一个进程，而用户对此没有感知。我们在九台服务器上每一台跑一个进程，只是为了发布版本和冗余的问题。

全局登录

整个项目中有一些看起来可以独立出来（事实上也是），不过也同属于整个大 HTTPS 迁移中的一部分。登录就是其中一个项目。我首先来说说这个，因为这比别它变化都要早上线。

在 Stack Overflow（及 Stack Exchange）的头五六年里，你登录的是一个个的独立网站。比如，`stackoverflow.com`、`stackexchange.com` 以及 `gaming.stackexchange.com` 都有它们自己的 cookies。值得注意的是：`meta.gaming.stackexchange.com` 的登录 cookie 是从 `gaming.stackexchange.com` 带过来的。这些是我们上面讨论证书时提到的 meta 站点。他们的登录信息是相关联的，你只能通过父站点登录。在技术上说并没有什么特别的，但考虑到用户体验就很糟糕了。你必须一个一个站登录。我们用「全局认证」的方法来[「修复」了这个问题](https://stackoverflow.blog/2010/09/11/global-network-auto-login/)，方法是在页面上放一个 `<iframe>`，内面访问一下 `stackauth.com`。如果用户在别处登录过的话，它也会在这个站点上登录，至少会去试试。这个体验还行，但是会有弹出框问你是否点击重载以登录，这样就又不是太好。我们可以做得更好的。对了，你也可以去问问 [Kevin Montrose](https://twitter.com/kevinmontrose) 关于移动 Safari 的匿名模式，你会震惊的。

于是我们有了「通用登录」。为什么用「通用」这个名字？因为我们已经用过「全局」了。我们就是如此单纯。所幸 cookies 也很单纯的东西。父域名里的 cookie（如 `stackexchange.com`）在你的浏览器里被带到所有子域名里去（如 `gaming.stackexchange.com`）。如果我们只二级域名的话，其实我们的域名并不多：

-   [askubuntu.com](https://askubuntu.com/)
-   [mathoverflow.net](https://mathoverflow.net/)
-   [serverfault.com](https://serverfault.com/)
-   [stackapps.com](https://stackapps.com/)
-   [stackexchange.com](https://stackexchange.com/)
-   [stackoverflow.com](https://stackoverflow.com/)
-   [superuser.com](https://superuser.com/)

是的，我们有一些域名是跳转到上面的列表中的，比如 [askdifferent.com](http://askdifferent.com/)。但是这些只是跳转而已，它们没有 cookies 也无需登录。

这里有很多细节的后端工作我没有提（归功于 [Geoff Dalgas](https://twitter.com/superdalgas) 和 [Adam Lear](https://twitter.com/aalear)），但大体思路就是，当你登录的时候，我们把这些域名都写入一个 cookie。我们是通过第三方的 cookie 和[随机数](https://en.wikipedia.org/wiki/Cryptographic_nonce)来做的。当你登录其中任意一个网站的时候，我们在页面上都会放 6 个 `<img>` 标签来往其它域名写入 cookie，本质上就完成了登录工作。这并不能在 *所有情况* 下都适用（尤其是移动 Safari 简直是要命了），但和之前比起来那是好得多了。

客户端的代码不复杂，基本上长这样：

```javascript
$.post('/users/login/universal/request', function (data, text, req) {
    $.each(data, function (arrayId, group) {
        var url = '//' + group.Host + '/users/login/universal.gif?authToken=' + 
            encodeURIComponent(group.Token) + '&nonce=' + encodeURIComponent(group.Nonce);
        $(function ( ) { $('#footer').append('<img style="display:none" src="' + url + '"></img>'); });
    });
}, 'json');
```

但是要做到这点，我们必须上升到账号级别的认证（之前是用户级别）、改变读取 cookie 的方式、改变这些 meta 站的登录工作方式，同时还要将这一新的变动整合到其它应用中。比如说，Careers（现在拆成了 Talent 和 Jobs）用的是另一份代码库。我们需要让这些应用读取相应的 cookies，然后通过 API 调用 Q&A 应用来获取账户。我们部署了一个 NuGet 库来减少重复代码。底线是：你在一个地方登录，就在所有域名都登录。不弹框，不重载页面。

技术的层面上看，我们不用再关心 `*.*.stackexchange.com` 是什么了，只要它们是 `stackexchange.com` 下就行。这看起来和 HTTPS 没有关系，但这让我们可以把 `meta.gaming.stackexchange.com` 变成 `gaming.meta.stackexchange.com` 而不影响用户。

本地 HTTPS 开发

要想做得更好的话，本地环境应该尽量与开发和生产环境保持一致。幸好我们用的是 IIS，这件事情还简单的。我们使用一个工具来设置开发者环境，这个工具的名字叫「本地开发设置」——单纯吧？它可以安装工具（Visual Studio、git、SSMS 等）、服务（SQL Server、Redis、Elasticsearch）、仓库、数据库、网站以及一些其它东西。做好了基本的工具设置之后，我们要做的只是添加 SSL/TLS 证书。主要的思路如下：

```
Websites = @(
    @{
        Directory = "StackOverflow";
        Site = "local.mse.com";
        Aliases = "discuss.local.area51.lse.com", "local.sstatic.net";
        Databases = "Sites.Database", "Local.StackExchange.Meta", "Local.Area51", "Local.Area51.Meta";
        Certificate = $true;
    },
    @{
        Directory = "StackExchange.Website";
        Site = "local.lse.com";
        Databases = "Sites.Database", "Local.StackExchange", "Local.StackExchange.Meta", "Local.Area51.Meta";
        Certificate = $true;
    }
)
```

我把使用到的代码[放在了一个 gist 上：`Register-Websites.psm1`](https://gist.github.com/NickCraver/6b5e75c153d60d0df5b0970d52412d4e)。我们通过 host 头来设置网站（通过别名添加），如果直连的话就给它一个证书（嗯，现在应该把这个行为默认改为 `$true` 了），然后允许 AppPool 账号来访问数据库，于是我们本地也在使用 `https://` 开发了。嗯，我知道我们应该把这个设置过程开源出来，不过我们仍需去掉一些专有的业务。会有这么一天的。

**为什么这件事情很重要？** 在此之前，我们从 `/content` 加载静态内容，而不是从另一个域名。这很方便，但也隐藏了类似于[跨域请求（CORS）](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)的问题。在同一个域名下用同一个协议能正常加载的资源，换到开发或者生产环境下就有可能出错。[「在我这里是好的。」](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)

当我们使用和生产环境中同样协议以及同样架构的 CDN 还有域名设置时，我们就可以在开发机器上找出并修复更多的问题。比如，你是否知道，从 `https://` 跳转到 `http://` 时，[浏览器是不会发送 referer](https://www.w3.org/Protocols/rfc2616/rfc2616-sec15.html#sec15.1.3) 的？这是一个安全上的问题，referer 头中可能带有以明文传输的敏感信息。

「Nick 你就扯吧，我们能拿到从 Google 拿到 referer 啊！」确实。但是这是因为他们*主动选择这一行为*。如果你看一下 Google 的搜索页面，你可以看到这样的 `<meta>` 指令：

    <meta content="origin" id="mref" name="referrer">

这也就是为什么你可以取到 referer。

好的，我们已经设置好了，现在该做些什么呢？

### 混合内容：来自于你们

混合内容是个筐，什么都能往里装。我们这些年下来积累了哪些混合内容呢？不幸的是，有很多。这个列表里我们必须处理的用户提交内容：

-   `http://` 图片，出现在[问题](https://stackoverflow.com/questions)、答案、[标签](https://stackoverflow.com/tags)、wiki 等内容中使用
-   `http://` 头像
-   `http://` 头像，出现在聊天中（站点侧边栏）
-   `http://` 图片，出现于个人资料页的「关于我」部分
-   `http://` 图片，出现于[帮助中心的文章中](https://stackoverflow.com/help)
-   `http://` YouTube 视频（有些站点启用了，比如 [gaming.stackexchange.com](https://gaming.stackexchange.com/)）
-   `http://` 图片，出现于[特权描述中](https://stackoverflow.com/help/privileges)
-   `http://` 图片，出现于[开发者故事中](http://stackoverflow.com/users/story/13249)
-   `http://` 图片，出现于[工作描述中](https://stackoverflow.com/jobs)
-   `http://` 图片，出现于[公司页面中](https://stackoverflow.com/jobs/companies)
-   `http://` 源地址，出现在[ JavaScript 代码中](https://meta.stackoverflow.com/q/269753/13249).

上面的每一个都带有自己独有的问题，我仅仅会覆盖一下值得一提的部分。注意：我谈论的每一个解决方案都必须扩展到我们这个架构下的几百个站点和数据库上。

在上面的所有情况中（除了代码片段），要消除混合内容的第一步工作就是：你必须先消除*新*的混合内容。否则，这个清理过程将会无穷无尽。要做到这一点，[我们开始全网强制仅允许内嵌 `https://` 图片](https://meta.stackexchange.com/q/291947/135201)。一旦这个完成之后，我们就可以开始清理了。

对于问题、答案以及其他帖子形式中，我们需要具体问题具体分析。我们先来搞定 90% 以上的情况：`stack.imgur.com`。在我来之前 Stack Overflow 就已经有自己托管的 Imgur 实例了。你在编辑器中上传的图片就会传到那里去。绝大部分的帖子都是用的这种方法，而他们几年前就为我们添加了 HTTPS 支持。所以这个就是一个很直接的查找替换（我们称为帖子 markdown 重处理）。

然后我们通过通过 [Elasticsearch](https://www.elastic.co/) 对所有内容的索引来找出所有剩下的文件。我说的我们其实指的是 [Samo](https://twitter.com/m0sa)。他在这里处理了大量的混合内容工作。当我们看到大部分的域名其实已经支持 HTTPS 了之后，我们决定：

1.  对于每个 `<img>` 的源地址都尝试替换成 `https://`。如果能正常工作则替换帖子中的链接
2.  如果源地址不支持 `https://`，将其转一个链接

当然，并没有那么顺利。我们发现用于匹配 URL 的正则表达式其实已经坏了好几年了，并且没有人发现……所以我们修复了正则，重新做了索引。

有人问我们：「为什么不做个代理呢？」呃，从法律和道德上来说，代理对我们的内容来说是个灰色地带。比如，我们 [photo.stackexchange.com](https://photo.stackexchange.com/) 上的摄像师会明确声明不用 Imgur 以保留他们的权利。我们充分理解。如果我们开始代理并缓存*全图*，这在法律上有点问题。我们后来发现在几百万张内嵌图片中，只有几千张即不支持 `https://` 也没有 404 失效的。这个比例（低于 1%）不足于让我们去搭一个代理。

我们确实*研究过*搭一个代理相关的问题。费用有多少？需要多少存储？我们的带宽足够吗？我们有了一个大体上的估算，当然有点答案也不是很确定。比如我们是否要用 Fastly，还是直接走运营商？哪一种比较快？哪一种比较便宜？哪一种可以扩展？这个足够写另一篇博客了，如果你有具体问题的话可以在评论里提出，我会尽力回答。

所幸，在这个过程中，为了解决几个问题，[balpha](https://twitter.com/balpha) 更改了用 HTML5 嵌入 YouTube 的方式。我们也就顺便强制了一下 YouTube 的 `https://` 嵌入。

剩下的几个内容领域的事情差不多：先阻止新的混合内容进来，再替换掉老的。这需要我们在下面几个领域进行更改：

-   帖子
-   个人资料
-   开发故事
-   帮助中心
-   职场
-   公司业务

声明：JavaScript 片段的问题仍然没有解决。这个有点难度的原因是：

1.  资源有可能不以 `https://` 的方式存在（比如一个库）
2.  由于这个是 JavaScript，你可以自己构建出任意的 URL。这里我们就无力检查了。
    -   如果你有更好的方式来处理这个问题，**请告诉我们**。我们在可用性与安全性上不可兼得。

### 混合内容：来自我们

并不是处理完用户提交的内容就解决问题了。我们自己还是有不少 `http://` 的地方需要处理。这些更改本身没什么特别的，但是这至少能解答「为什么花了那么长时间？」这个问题：

-   广告服务（Calculon）
-   广告服务（Adzerk）
-   标签赞助商
-   JavaScript 假定
-   Area 51（这代码库也太老了）
-   分析跟踪器（Quantcast, GA）
-   每个站点引用的 JavaScript（社区插件）
-   `/jobs` 下的所有东西（这其实是个代理）
-   用户能力
-   ……还有代码中所有出现 `http://` 的地方

JavaScript 和链接比较令人痛苦，所以我在这里稍微提一下。

JavaScript 是一个不少人遗忘的角落，但这显然不能被无视。我们不少地方将主机域名传递给 JavaScript 时假定它是 `http://` ，同时也有不少地方写死了 meta 站里的 `meta.` 前缀。很多，真的很多，救命。还好现在已经不这样了，我们现在用服务器渲染出一个站点，然后在页面顶部放入相应的选择：

```javascript
StackExchange.init({
  "locale":"en",
  "stackAuthUrl":"https://stackauth.com",
  "site":{
    "name":"Stack Overflow"
    "childUrl":"https://meta.stackoverflow.com",
    "protocol":"http"
  },
  "user":{
    "gravatar":"<div class=\"gravatar-wrapper-32\"><img src=\"https://i.stack.imgur.com/nGCYr.jpg\"></div>",
    "profileUrl":"https://stackoverflow.com/users/13249/nick-craver"
  }
});
```

这几年来我们在代码里也用到了很多静态链接。比如，在页尾，在页脚，在帮助区域……到处都是。对每一个来说，解决方式都不复杂：把它们改成 `<site>.Url("/path")` 的形式就好了。不过要找出这些链接有点意思，因为你不能直接搜 `"http://"`。感谢 W3C 的丰功伟绩：

```
<svg xmlns="http://www.w3.org/2000/svg"...
```

是的，这些是标识符，是不能改的。所以我希望 Visual Studio 在查找文件框中增加一个「排除文件类型」的选项。Visual Studio 你听见了吗？VS Code 前段时间就加了这个功能。我这要求不过分。

这件事情很枯燥，就是在代码中找出一千个链接然后替换而已（包括注释、许可链接等）。但这就是人生，我们必须要做。把这些链接改成 `.Url()` 的形式之后，一旦站点支持 HTTPS 的时候，我们就可以让链接动态切换过去。比如我们得等到 `meta.*.stackexchange.com` 搬迁完成之后再进行切换。插播一下我们数据中心的密码是「煎饼馃子」拼音全称，应该没有人会读到这里吧，所以在这里存密码很安全。当站点迁完之后，`.Url()` 仍会正常工作，然后用 `.Url()` 来渲染默认为 HTTPS 的站点也会继续工作。这将静态链接变成了动态。

另一件重要的事情：这让我们的开发和本地环境都能正常工作，而不仅仅是链到生产环境上。这件事情虽然枯燥，但还是值得去做的。对了，因为我们的规范网址（canonical）也通过 `.Url()` 来做了，所以一旦用户开始用上 HTTPS，Google 也可以感知到。

一旦一个站点迁到 HTTPS 之后，我们会让爬虫来更新站点链接。我们把这个叫修正「Google 果汁」，同时这也可以让用户不再碰到 301。

### 跳转（301）

当你把站点移动到 HTTPS 之后，为了和 Google 配合，你有两件重要的事情要做：

-   更新规范网址，比如 `<link rel="canonical" href="https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454" />`
-   把 `http://` 链接通过 301 跳转至 `https://`

这个不复杂，也不是浩大的工程，但这非常*非常*重要。Stack Overflow 大部分的流量都是从 Google 搜索结果中过来的，所以我们得保证这个不产生负面影响。这个是我们的生计，如果我们因此丢了流量那我真是要失业了。还记得那些 `.internal` 的 API 调用吗？对，我们同样不能把*所有东西*都进行跳转。所以我们在处理跳转的时候需要一定的逻辑（比如我们也不能跳转 `POST` 请求，因为浏览器处理得不好），当然这个处理还是比较直接的。这里是实际上用到的代码：

```javascript
public static void PerformHttpsRedirects()
{
    var https = Settings.HTTPS;
    // If we're on HTTPS, never redirect back
    if (Request.IsSecureConnection) return;

    // Not HTTPS-by-default? Abort.
    if (!https.IsDefault) return;
    // Not supposed to redirect anyone yet? Abort.
    if (https.RedirectFor == SiteSettings.RedirectAudience.NoOne) return;
    // Don't redirect .internal or any other direct connection
    // ...as this would break direct HOSTS to webserver as well
    if (RequestIPIsInternal()) return;

    // Only redirect GET/HEAD during the transition - we'll 301 and HSTS everything in Fastly later
    if (string.Equals(Request.HttpMethod, "GET", StringComparison.InvariantCultureIgnoreCase)
        || string.Equals(Request.HttpMethod, "HEAD", StringComparison.InvariantCultureIgnoreCase))
    {
        // Only redirect if we're redirecting everyone, or a crawler (if we're a crawler)
        if (https.RedirectFor == SiteSettings.RedirectAudience.Everyone
            || (https.RedirectFor == SiteSettings.RedirectAudience.Crawlers && Current.IsSearchEngine))
        {
            var resp = Context.InnerHttpContext.Response;
            // 301 when we're really sure (302 is the default)
            if (https.RedirectVia301)
            {
                resp.RedirectPermanent(Site.Url(Request.Url.PathAndQuery), false);
            }
            else
            {
                resp.Redirect(Site.Url(Request.Url.PathAndQuery), false);
            }
            Context.InnerHttpContext.ApplicationInstance.CompleteRequest();
        }
    }
}
```


注意我们并不是默认就跳 301（有一个 `.RedirectVia301` 设置)，因为我们做一些会产生永久影响的事情之前必须仔细测试。我们会[晚一点](#hsts-preloading)来讨论 [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) 以及后续影响。

### Websockets

这一块会过得快一点。Websocket 不难，从某种角度来说，这是我们做过的最简单的事情。我们用 websockets 来处理实时的用户影响力变化、收件箱通知、新问的问题、新增加的答案等等。这也就说基本上每开一个 Stack Overflow 的页面，我们都会有一个对应的 websocket 连接连到我们的负载均衡器上。

所以怎么改呢？其实很简单：安装一个证书，监听 `:443` 端口，然后用 `wss://qa.sockets.stackexchange.com` 来代替 `ws://` 。后者其实早就做完了（我们用了一个专有的证书，但是这不重要）。从 `ws://` 到 `wss://` 只是配置一下的问题。一开始我们还用 `ws://` 作为 `wss://` 的备份方案，不过后来就变成*仅用* `wss://` 了。这么做有两个原因：

1. 不用的话在 `https://` 下面会有混合内容警告
2. 可以支持更多用户。因为很多老的代理不能很好地处理 websockets。如果使用加密流量，大多数代理就只是透传而不会弄乱流量。对移动用户来说尤其是这样。

最大的问题就是：「我们能处理了这个负载吗？」我们全网处理了不少并发 websocket，在我写这估的时候我们有超过 600000 个**并发**的连接。这个是我们 HAProxy 的仪表盘在 [Opserver](https://github.com/opserver/Opserver) 中的界面：

[![HAProxy Websockets](/images/upload_dropbox/201709/HTTPS-Websockets.png)](../../static/images/upload_dropbox/201709/HTTPS-Websockets.png)

不管是在终端、抽象命名空间套接字还是前端来说都有很多连接。由于启用了 [TLS 会话恢复](https://tools.ietf.org/html/rfc5077)，HAProxy 本身的负载也很重。要让用户下一次重新连接更快，第一次协商之后用户会拿到一个令牌，下一次会把这个令牌发送过来。如果我们的内存足够并且没有超时，我们会恢复上次的会话而不是再开一个。这个操作可以节省 CPU，对用户来说有性能提升，但会用到到更多内存。这个多因 key 大小而异（2048，4096 或是更多？）我们现在用的是 4096 位的 key。在开了 600000 个 websocket 的情况下，我们只用掉了负载均衡器 64GB 内存里的 19GB。这里面 12GB 是 HAProxy 在用，大多数为 TLS 会话缓存。所以结果来说还不错，如果*我们不得不买内存的话*，这也会是整个 HTTPS 迁移中最便宜的东西。

[![HAProxy Websocket Memory](/images/upload_dropbox/201709/HTTPS-WebsocketMemory.png)](../../static/images/upload_dropbox/201709/HTTPS-WebsocketMemory.png)

### 未知

我猜现在可能是我们来谈论一些未知问题的时候。有些问题是在我们尝试之前无法真正知道的：

- Google Analytics 里的流量表现怎么样？（我们会失去 referer 吗？）
- Google Webmasters 的转换是否平滑？（301 生效吗？规范域名呢？要多长时间？）
- Google 搜索分析会怎么工作（我们会在搜索分析中看到 `https://` 吗？）
- 我们搜索排名会下降吗？（最恐怖的）

有很多人都谈过他们转化成 `https://` 的心得，但对我们却有点不一样。我们不是一个站点。我们是多个域名下的多个站点。我们不知道 Google 会怎么对待我们的网络。它会知道 `stackoverflow.com` 和 `superuser.com` 有关联吗？不知道。我们也不能指望 Google 来告诉我们这些。

所以我们就做测试。在我们[全网发布](https://meta.stackexchange.com/q/292058/135201) 中，我们测试了几个域名：

- [meta.stackexchange.com](https://meta.stackexchange.com/)
- [security.stackexchange.com](https://security.stackexchange.com/)
- [superuser.com](https://superuser.com/)

对，这些是 Samo 和我会了仔细讨论出来的结果，花了有三分钟那么久吧。Meta 是因为这是我们最重要的反馈网站。Security 站上有很多专家可能会注意到相关的问题，特别是 HTTPS 方面。最后一个，Super User，我们需要知道搜索对我们内容的影响。比起 meta 和 security 来说法，Super User 的流量要大得多。最重要的是，它有*来自 Google* 的原生流量。

我们一直在观察并评估搜索的影响，所以 Super User 上了之后其他网站过了很久才跟上。到目前为止我们能说的是：基本上没影响。搜索、结果、点击还有排名的周变化都在正常范围内。我们公司*依赖*于这个流量，这对我们真的很重要。所幸，没有什么值得我们担心的点，我们可以继续发布。

### 错误

如果不提到我们搞砸的部分，这篇文章就还不够好。错误永远是个选择。让我们来总结一下这一路让我们后悔的事情：

#### 错误：相对协议 URL

如果你的一个资源有一个 URL 的话，一般来说你会看到一些 `http://example.com` 或者 `https://example.com` 之类的东西，包括我们图片的路径等等。另一个选项就是你可以使用 `//example.com`。这被称为[相对协议 URL](https://en.wikipedia.org/wiki/Wikipedia:Protocol-relative_URL)。我们很早之前就在图片、JavaScript、CSS 等中这么用了（我们自有的资源，不是指用户提交）。几年后，我们发现这不是一个好主意，至少对我们来说不是。相对协议链接中的「相对」是*对于页面而言*。当你在 `http://stackoverflow.com` 时，`//example.com` 指的是 `http://example.com`；如果你在 `https://stackoverflow.com` 时，就和 `https://example.com` 等同。那么这个有什么问题呢？

问题在于，图片 URL 不仅是用在页面中，它们还用在邮件、API 还有移动应用中。当我们理了一下路径结构然后在到处都使用图片路径时我们发现不对了。虽然这个变化极大降低了代码冗余，并且简化了很多东西，结果却是我们在邮件中使用了相对 URL。绝大多数邮件客户端都不能处理相对协议 URL 的图片。因为它们不知道是什么协议。Email 不是 `http://` 也不是 `https://`。只有你在浏览器里查看邮件，有可能是预期的效果。

那该怎么办？我们把所有的地方都换成了 `https://`。我把我们所有的路径代码统一到两个变量上：CDN 根路径，和对应特定站点的文件夹。例如 Stack Overflow 的样式表在 [`https://cdn.sstatic.net/Sites/stackoverflow/all.css`](https://cdn.sstatic.net/Sites/stackoverflow/all.css) 上（当然我们有缓存中断器），换成本地就是 `https://local.sstatic.net/Sites/stackoverflow/all.css`。你能看出其中的共同点。通过拼接路径，逻辑简单了不少。则　通过强制 `https://`，用户还可以在整站切换之前就享受 HTTP/2 的好处，因为所有静态资源都已经就位。都用 `https://` 也表示我们可以在页面、邮件、移动还有 API 上使用**同一个**属性。这种统一也意味着我们有一个固定的地方来处理所有路径——我们到处都有缓存中断器。

注意：如果你像我们一样中断缓存，比如 `https://cdn.sstatic.net/Sites/stackoverflow/all.css?v=070eac3e8cf4`，请不要用构建号。我们的缓存中断使用的是文件的[校验值](https://en.wikipedia.org/wiki/Checksum)，也就是说只有当文件真正变化的时候你才会下载一个新的文件。用构建号的话可能会稍微简单点，但同时也会对你的费用还有性能有所损伤。

能做这个当然很好，可我们为什么不从一开始就做呢？因为 HTTPS 在那个时候性能还不行。用户通过 `https://` 访问会比 `http://`慢很多。举一个大一点的例子：我们上个月在 `sstatic.net` 上收到了四百万个请求，总共有 94TB。如果 HTTPS 性能不好的话，这里累积下来的延迟就很可观了。不过因为我们上了 HTTP/2，以及设置好 CDN/代理层，性能的问题已经好很多了。对于用户来说更快了，对我们来说则更简单，何乐不为呢！

#### 错误：API 及 .internal

当我们把代理架起来开始测试的时候发现了什么？我们忘了一件很重要的事，准确地说，我忘了一件很重要的事。我们在内部 API 里大量地使用了 HTTP。当然这个是正常工作的，只是它们变得更慢、更复杂、也更容易出问题了。

比方说一个内部 API 需要访问 `stackoverflow.com/some-internal-route`，之前，节点是这些：

- 原始 app
- 网关/防火墙（暴露给公网）
- 本地负载均衡器
- 目标 web 服务器

这是因为我们是可以解析 `stackoverflow.com` 的，解析出来的 IP 就是我们的负载均衡器。当有代理的情况下，为了让用户能访问到最近的节点，他们访问到的是不同的 IP 和目标点。他们的 DNS 解析出来的 IP 是 CDN/代理层 (Fastly)。糟了，这意识着我们现在的路径是这样的：

- 原始 app
- 网关/防火墙（暴露给公网）
- 我们的外部路由器
- 运营商（多节点）
- 代理（Cloudflare/Fastly）
- 运营商（到我们的代理路）
- 我们的外部路由器
- 本地负载均衡器
- 目标 web 服务器

嗯，这个看起来更糟了。为了实现一个从 A 调用一下 B，我们多了很多不必要的依赖，同时性能也下降了。我不是说我们的代理很慢，只是原本只需要 1ms 就可以连到我们数据中心……好吧，我们的代理很慢。

我们内部讨论了多次如何用最简单的方法解决这个问题。我们可以把请求改成 `internal.stackoverflow.com`，但是这会产生可观的修改（也许也会产生冲突）。我们也创建一个 DNS 来专门解析内部地址（但这样会产生通配符继承的问题）。我们也可以在内部把 `stackoverflow.com` 解析成不同的地址（这被称为[水平分割 DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS)），但是这一来不好调试，二来在多数据中心的场景下不知道该到哪一个。

最终，我们在所有暴露给外部 DNS 的域名后面都加了一个 `.internal` 后续。比如，在我们的网络中，`stackoverflow.com.internal` 会解析到我们的负载均衡器后面（DMZ）的一个内部子网内。我们这么做有几个原因：

- 我们可以在内部的 DNS 服务器里覆盖且包含一个顶级域名服务器（活动目录）
- 当请求从 HAProxy 传到 web 应用中时，我们可以把 `.internal` 从 `Host` 头中移除（应用层无感知）
- 如果我们需要内部到 DMZ 的 SSL，我们可以用一个类似的通配符组合
- 客户端 API 的代码很简单（如果在域名列表中就加一个 `.internal`）

我们客户端的 API 代码是大部分是由 [Marc Gravell](https://twitter.com/marcgravell) 写的一个 `StackExchange.Network` 的 NuGet 库。对于每一个要访问的 URL，我们都用静态的方法调用（所以也就只有通用的获取方法那几个地方）。如果存在的话就会返回一个「内部化」URL，否则保持不变。这意味着一次简单的 NuGet 更新就可以把这个逻辑变化部署到所有应用上。这个调用挺简单的：

\# uri = SubstituteInternalUrl(uri);


这里是 `stackoverflow.com` DNS 行为的一个例子：

* Fastly：151.101.193.69, 151.101.129.69, 151.101.65.69, 151.101.1.69
* 直连（外部路由）：198.252.206.16
* 内部：10.7.3.16

记得我们之前提到的 [dnscontrol](https://github.com/StackExchange/dnscontrol) 吗？我们可以用这个快速同步。归功于 JavaScript 的配置/定义，我们可以简单地共享、简化代码。我们匹配所有所有子网和所有数据中心中的所有 IP 的最后一个字节，所以用几个变量，所有 AD 和外部的 DNS 条目都对齐了。这也意味着我们的 HAProxy 配置更简单了，基本上就是这样：

```
stacklb::external::frontend_normal { 't1_http-in':
  section_name    => 'http-in',
  maxconn         => $t1_http_in_maxconn,
  inputs          => {
    "${external_ip_base}.16:80"  => [ 'name stackexchange' ],
    "${external_ip_base}.17:80"  => [ 'name careers' ],
    "${external_ip_base}.18:80"  => [ 'name openid' ],
    "${external_ip_base}.24:80"  => [ 'name misc' ],
```


综上，API 路径更快了，也更可靠了：

- 原始 app
- 本地负载均衡器（DMZ）
- 目标 web 服务器

我们解决了几个问题，还剩下几百个等着我们。

#### 错误：301 缓存

在从 `http://` 301 跳到 `https://` 时有一点我们没有意识的是，Fastly 缓存了我们的返回值。在 Fastly 中，[默认的缓存键](https://docs.fastly.com/guides/vcl/manipulating-the-cache-key)并不考虑协议。我个人不同意这个行为，因为在源站默认启用 301 跳转会导致无限循环。这个问题是这样造成的：

1. 用户访问 `http://` 上的一个网络
2. 通过 301 跳转到了 `https://`
3. Fastly 缓存了这个跳转
4. 任意一个用户（包括 #1 中的那个）以 `https://` 访问同一个页面
5. Fastly 返回一个跳至 `https://` 的 301，尽量你已经在这个页面上了

这就是为什么我们会有无限循环。要解决这个问题，我们得关掉 301，清掉 Fastly 缓存，然后开始调查。Fastly [建议我们在 vary 中加入 `Fastly-SSL`](https://docs.fastly.com/guides/vcl/manipulating-the-cache-key#purging-adjustments-when-making-additions-to-cache-keys)，像这样：

```
sub vcl_fetch {
  set beresp.http.Vary = if(beresp.http.Vary, beresp.http.Vary ",", "") "Fastly-SSL";
```

在我看来，这应该是默认行为。

错误：帮助中心的小插曲

记得我们必须修复的帮助文档吗？帮助文档都是按语言区分，只有极少数是按站点来分，所以本来它们是可以共享的。为了不产生大量重复代码及存储结构，我们做了一点小小的处理。我们把实际上的帖子对象（和问题、答案一样）存在了 `meta.stackexchange.com` 或者是这篇帖子关联的站点中。我们把生成的 `HelpPost` 存在中心的 `Sites` 数据库里，其实也就是生成的 HTML。在处理混合内容的时候，我们也处理了单个站里的帖子，简单吧！

当原始的帖子修复后，我们只需要为每个站点去再生成 HTML 然后填充回去就行了。但是这个时候我犯了个错误。回填的时候拿的是*当前站点*（调用回填的那个站点），而不是原始站。这导致 `meta.stackexchange.com` 里的 12345 帖子被 `stackoverflow.com` 里的 12345 帖子所替代。有的时候是答案、有的时候是问题，有的时候有一个 tag wiki。这也导致了一些[很有意思的帮助文档](https://meta.stackoverflow.com/q/345280/13249)。这里有一些[相应的后果](https://meta.stackoverflow.com/a/345282/13249)。

我只能说，还好修复的过程挺简单的：

 

[![Me being a dumbass](/images/upload_dropbox/201709/HTTPS-HelpCommit.png)](../../static/images/upload_dropbox/201709/HTTPS-HelpCommit.png)

再一次将数据填充回去就能修复了。不过怎么说，这个当时算是在公共场合闹了个笑话。抱歉。

### 开源

这里有我们在这个过程中产出的项目，帮助我们改进了 HTTPS 部署的工作，希望有一天这些能拯救世界吧：

-   [BlackBox](https://github.com/StackExchange/blackbox) （在版本控制中安全存储私密信息）作者 [Tom Limoncelli](https://twitter.com/yesthattom)
-   [capnproto-net](https://github.com/StackExchange/capnproto-net)（不再支持 —— .NET 版本的 [Cap’n Proto](https://capnproto.org/)）作者 [Marc Gravell](https://twitter.com/marcgravell)
-   [DNSControl](https://github.com/StackExchange/dnscontrol)（控制多个 DNS 提供商）作者 [Craig Peterson](https://twitter.com/captncraig) and [Tom Limoncelli](https://twitter.com/yesthattom)
-   [httpUnit](https://github.com/StackExchange/httpunit) （网站集成测试） 作者 [Matt Jibson](https://twitter.com/mjibson) and [Tom Limoncelli](https://twitter.com/yesthattom)
-   [Opserver](https://github.com/opserver/Opserver) （支持 Cloudflare DNS） 作者 [Nick Craver](https://twitter.com/Nick_Craver)
-   [fastlyctl](https://github.com/alienth/fastlyctl)（Go 语言的 Fastly API 调用）作者 [Jason Harvey](https://twitter.com/alioth)
-   [fastly-ratelimit](https://github.com/alienth/fastly-ratelimit)（基于 Fastly syslog 流量的限流方案）作者 [Jason Harvey](https://twitter.com/alioth/)

### 下一步

我们的工作并没有做完。接下去还有一此要做的：

-   我们要修复我们聊天域名下的混合内容，如 [chat.stackoverflow.com](https://chat.stackoverflow.com/)，这里有用户嵌入的图片等
-   如果可能的话，我们把所有适用的域名加进 [Chrome HSTS 预加载列表](https://hstspreload.org/)
-   我们要评估 [HPKP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning) 以及我们是否想部署（这个很危险，目前我们倾向于不部署）
-   我们需要把聊天移到 `https://`
-   我们需要把所有的 cookies 迁移成安全模式
-   我们在等能支持 HTTP/2 的 HAProxy 1.8（大概在九月出来）
-   我们需要利用 HTTP/2 的推送（我会在六月与 Fastly 讨论这件事情——他们还现在不支持跨域名推送）
-   我们需要把 301 行为从 CDN/代理移出以达到更好的性能（需要按站点发布）

HSTS 预加载

[HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) 指的是「HTTP 严格传输安全」。OWASP 在[这里](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet)有一篇很好的总结。这个概念其实很简单：

-   当你访问 `https://` 页面的时候，我们给你发一个这样的头部：`Strict-Transport-Security: max-age=31536000`
-   在这个时间内（秒），你的浏览器只会通过 `https://` 访问这个域名

哪怕你是点击一个 `http://` 的链接，你的浏览器也会*直接*跳到 `https://`。哪怕你有可能已经设置了一个 `http://` 的跳转，但你的浏览器不会访问，它会直接访问 SSL/TLS。这也避免了用户访问不安全的 `http://` 而遭到劫持。比如它可以把你劫持到一个 `https://stack<长得很像o但实际是个圈的unicode>verflow.com` 上，那个站点甚至有可能部好了 SSL/TLS 证书。只有不访问这个站点才是安全的。

但这需要我们至少访问一次站点，然后才能有这个头部，对吧？对。所以我们有 [HSTS 预加载](https://hstspreload.org/)，这是一个域名列表，随着所有主流浏览器分发且由它们预加载。也就是说它们在第一次访问的时候就会跳到 `https://` 去，所以**永远不会**有任何 `http://` 通信。

很赞吧！所以要怎么才能上这个列表呢？这里是要求：

1.  要有一个有效的证书
2.  如果你监听 80 端口的话，HTTP 应该跳到同一个主机的 HTTPS 上
3.  所有子域名都要支持 HTTPS
4.  特别是如果有 DNS 纪录的话，www 子域名要支持 HTTPS
5.  主域名的 HSTS 头必要满足如下条件：
6.  max-aget 至少得是十八周（10886400 秒）
7.  必须有 includeSubDomains 指令
8.  必须指定 preload 指令
9.  如果你要跳转到 HTTPS 站点上，跳转也必须有 HSTS 头部（而不仅仅是跳过去的那个页面）

这听起来还行吧？我们所有的活跃域名都支持 HTTPS 并且有有效的证书了。不对，我们还有一个问题。记得我们有一个 `meta.gaming.stackexchange.com` 吧，虽然它跳到 `gaming.meta.stackexchange.com`，但这个跳转本身并没有有效证书。

以 meta 为例，如果我们在 HSTS 头里加入 `includeSubDomains` 指令，那么网上所有指向旧域名的链接都会踩坑。它们本该跳到一个 `http:///` 站点上（现在是这样的），一旦改了就会变成一个非法证书错误。昨天我们看了一下流量日志，每天仍有 8 万次访问的是通过 301 跳到 meta 子域上的。这里有很多是爬虫，但还是有不少人为的流量是从博客或者收藏夹过来的……而有些爬虫真的很蠢，从来不根据 301 来更新他们的信息。嗯，你还在看这篇文章？我自己写着写着都已经睡着 3 次了。

我们该怎么办呢？我们是否要启用 SAN 证书，加入几百个域名，然后调整我们的基础架构使得 301 跳转也严格遵守 HTTPS 呢？如果要通过 Fastly 来做的话就会提升我们的成本（需要更多 IP、证书等等）。[Let’s Encrypt](https://letsencrypt.org/) *倒是*真的能帮上点忙。获取证书的成本比较低，如果你不考虑设置及维护的人力成本的话（因为我们由于[上文所述](#certificates)内容并没有在使用它).

还有一块是上古遗留问题：我们内部的域名是 `ds.stackexchange.com`。为什么是 `ds.`？我不确定。我猜可能是我们不知道怎么拼 data center 这个词。这意味着 `includeSubDomains` 会自动包含*所有内部终端*。虽然我们大部分都已经上了 `https://` ，但是如果什么都走 HTTPS 会导致一些问题，也会带来一定延时。不是说我们不想在内部也用 `https://`，只不过这是一个整体的项目（大部分是证书分发和维护，还有多级证书），我们不想增加耦合。那为什么不改一下内部域名呢？主要还是时间问题，这一动迁需要大量的时间和协调。

目前，我们将 HSTS 的 `max-age` 设为两年，并且**不包括** `includeSubDomains`。除非迫不得以，我不会从代码里移除这个设定，因为它太危险了。一旦我们把所有 Q&A 站点的 HSTS 时间都设置好之后，我们会和 Google 聊一下是不是能在不加 `includeSubDomains` 的情况下把我们加进 HSTS 列表中，至少我们会试试看。你可以看到，虽然很罕见，但[目前的这份列表中](https://chromium.googlesource.com/chromium/src/net/+/master/http/transport_security_state_static.json)还是出现了这种情况的。希望从加强 Stack Overflow 安全性的角度，他们能同意这一点。

聊天

为了尽快启用 [`安全` cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#Secure_and_HttpOnly_cookies)（仅在 HTTPS 下发送），我们会将聊天（[chat.stackoverflow.com](https://chat.stackoverflow.com/)、\[[chat.stackexchange.com](http://chat.stackexchange.com/)及 [chat.meta.stackexchange.com](https://chat.meta.stackexchange.com/)）跳转至 `https://`。 正如我们的通用登录所做的那样，聊天会依赖于二级域名下的 cookie。如果 cookie 仅在 `https://` 下发送，你就只能在 `https://` 下登录。

这一块有待斟酌，但其实在有混合内容的情况下将聊天迁至 `https://` 是一件好事。我们的网络更加安全了，而我们也可以处理实时聊天中的混合内容。希望这个能在接下去的一两周之内实施，这在我的计划之中。

今天

不管怎么说，这就是我们今天到达的地步，也是我们过去四年中一直在做的事情。确实有很多更高优先级的事情阻挡了 HTTPS 的脚步——这也远远不是我们唯一在做的事情。但这就是生活。做这件事情的人们还在很多你们看不见的地方努力着，而涉及到的人也远不止我所提到的这些。在这篇文章中我只提到了一些花了我们很多时间的、比较复杂的话题（否则就会太长了），但是这一路上不管是 Stack Overflow 内部还是外部都有很多人帮助过我们。

我知道你们会有很多的疑问、顾虑、报怨、建议等等。我们非常欢迎这些内容。本周我们会关注底下的评论、我们的 meta 站、Reddit、Hacker News 以及 Twitter，并尽可能地回答/帮助你们。感谢阅读，能全文读下的来真是太棒了。（比心）

