---
title: "软件开发中的角色扮演"
author: "alswl"
slug: "software-development-in-the-role-playing"
date: "2010-01-09T00:00:00+08:00"
tags: ["软件开发和项目管理"]
categories: ["managment"]
---

说到软件开发的过程、环节等等，我印象里只剩下一大堆术语和一些流程的大概，但是因为缺乏正规开发的经验，所以并没有对软件开发中每个人的角色有深入理解，今天在周末
检查Delicious Temp标签时候，看到 [圆木菠萝头](http://blog.boluotou.com/)
的这片文章，收获颇丰，现在转载与大家分享。

原文链接：[ 软件开发中的角色扮演 - 软件开发 - 圆木菠萝罐](http://blog.boluotou.com/Developer/2009/06/S
oftware_Role) （我稍微调了一下格式，没有修改文章内容 ^_^）

××××××XXX分哥线XXX×××××××

商业软件开发并不是只有一个编程的人，而是可以分为不同的角色。

不同的软件公司因为规模大小性质各不相同，所以围绕软件的角色也各不相同。这就好比在重点学校里面分级很明确，每科有个老师，每个年级每个班级都有各自的老师，也有主
任书记校长支持角色。而在电影《一个都不能少》级别的学校里面，往往一个老师兼职从语文教到体育，年级从一年级到六年级。类似的说，一个大型的软件外包企业，外资企业
，往往分工明确细致，每个人像螺丝钉一样在一起工作，让整个大机器得以运转。而在一个小型创业企业里面，往往一个人从接触客户，到开发产品到交付产品＊＊＊走完，整个
产品周期就一个人，甚至几个产品周期就一个人。

所以解释角色要针对性。远的不说，就拿我们的项目组来举例。我们项目组可以说一共有5种角色，开发（DEV），测试（QA），质量监督（SQA），技术主管
（Tech-Lead）,开发经理（SDM）。

## 1. 开发 （DEV）

编程能力 ★★★★★

业务认知 ★★☆

沟通能力 ★★☆

管理能力 N/A

全局观 N/A

开发就是大家经常说的编程的人。工作主要是写代码，其次是跟团队成员客户沟通。前后者比例大概是7：3的关系。开发是整个软件开发团队当中的最重要的角色之一，道理很
简单，产品出自于他们的亲手。说到开发，大家的印象就是整天呆在电脑面前，目光呆滞，头发凌乱的计算机人士。确实，整天和计算机打交道的人的确容易变成这样，因为开发
首要解决的问题就是如何用技术能力去解决客户的需求，而不是自己的形象怎么样。事实上这种情况在现代中得到很大改善，很多IT人士都很注重自身形象。

具体的工作不仅要写代码用算法实现业务逻辑，更要有程序设计的思想，大到整个的程序框架，小到某个小模块的扩展性兼容性，都是在开发真正写代码之前着重要考虑的方面。

现在的编程不像以前打孔式编程那么艰涩，大厂商开发的强大的编程工具（IDE）让编程事半功倍。然而技术在变简单的同时，客户需求又在日趋复杂化。而技术就是为了实现
业务逻辑，将业务逻辑抽象建模用计算机程序的方式表现出来，所以一个不懂业务逻辑的开发不会了解模块和模块之间如何协同工作，这便给工作带来很大的局限性。而如果一个
开发只关注每个模块之内的细节实现，那在现实中便不是一个好开发，至少不是一个好用的开发。

沟通方面，开发需要和测试，技术主管，开发经理，甚至客户方面沟通，所以必要的沟通能力还是很需要的。现在的软件不再是一个人在战斗，在团队作战中，开发有时需要和测
试讨论"某个软件Bug（缺陷）是不是Bug"，有时需要和技术主管讨论客户的某个需求到底是要实现什么内容，有时需要和开发经理讨论项目的进度是否需要推迟。

就开发的工作本身而言，是不太需要管理能力和全局观的，如果能够做好编程的工作之外，这两方面也比较强，可能就离升职加薪不远了。

## 2. 测试（QA）

编程能力 ★★☆

业务认知 ★★★★

沟通能力 ★★★

管理能力 N/A

全局观 ★☆

任何一个产品都需要测试，就好比制造业中如果生产了一批电灯，我们不能听制灯师傅说信得过而信得过，而得通过一系列模拟用户的行为来对电灯进行测试，指标合格后方可出
厂投入市场。

软件测试也一样，需要对开发者开发出来的模块，产品进行全方位的测试。

原则是"做正确的事"，让客户需求功能得到满足。

基本做事方法就是模拟客户的一切日常行为，包括一些极其变态的行为，考验软件在各个方面的情况下的可用性和稳定性。而这些"日常行为"便称之为测试用例（Test
case），一个好的QA会设计出一套可以覆盖所有检查点（check point），又不重叠的测试用例，这套功底可以参考MECE方法。既然如此，QA就需要对整
个软件的业务相当熟悉，因为她（他）要知道在某个用户行为下，软件是否做出了正确的反应。

既然是模拟用户行为，那么QA就需要去手动"跑"测试用例。当一个系统很大的时候，测试用例极其多，光用手点一遍是非常耗费时间和人力的，所以QA可以做自动化测试。
所谓自动化，便是QA编写一些脚本代码，让计算机帮助去实现一些人为的行为，而不用自己手动点。所以这就需要QA做有一些代码编写能力。

测试方面有个重要的概念是黑盒测试和白盒测试。简单的说，黑盒测试就是在软件界面上用手点，不管后面的代码写得怎么样，只要我点击某个按钮或者其他元件的时候，结果是
我想要的就OK。所以叫"黑盒"，意思是看不到"里面的代码"。而白盒测试就是要直接审阅（review）代码，通过看代码发现业务逻辑，代码效率，后台数据操作等等
，可以说比黑盒测试要细致得多，当然成本可能也更多。所以叫"白盒"，意思是透明的盒子，可以看到里面的代码。所以，白盒测试是需要QA有一定的编程能力的。

沟通方面，QA经常要和DEV讨论Bug（软件缺陷），Bug的意思是本应该有的功能却没有做到的功能。对于某些比较似是而非的Bug, 怎么能够让开发者心服口服地
承认并去修复往往需要花费一番口舌。而这些Bug往往是根据不同的人的价值观认定是不是Bug，所以合理地传递价值观也是QA的一个基本素质。现实的一个案例是，公司
某QA"传递价值观"能力极强，于是被拉去做市场去了。除此之外，QA还要经常和技术主管沟通，熟悉客户需求。

全局观是因为QA要做集成测试，这样需要对产品本身有个全局的观念。比如产品有个用户管理系统和订单管理系统，那么对于"删除一个用户"的行为，用户的订单会怎么处理
？这便是一个全局观的意识。往往一个好的QA在这点上可以帮用户想到很多用户没想到的东西。

## 3. 质量监督（SQA）

编程能力 N/A

业务认知 ★

沟通能力 ★★★☆

管理能力 ★★★

全局观 ★★☆

如果说QA的作用是确保"做正确的事"，那么SQA的作用就是确保"正确的做事"。

通常SQA是不会直接参与软件开发的工作中，而是通过在一旁监督软件开发的过程，然后把监测的结果反馈给软件开发团队。

既然是监督过程，所以SQA经常是流程化的代名词。流程是外企当中比较看重的东西，从每天的Daily report, 到每周的weekly meeting，从什
么时候把当天的结果存到服务器上，到为什么团队出现重大事故，几乎都会有SQA的参与。所以在前期制定一个符合项目的流程是SQA的必然工作。项目运行过程中，所有项
目流程规定的点所涉及到的邮件都要CC一份给SQA。

当SQA通过流程观察项目的运行情况的时候，必然会收集到很多数据（包括刚才提到的邮件）。SQA会对这些数据进行统计归纳，然后总结出规律和报告直接递交给总监（D
irector）。鉴于此，SQA在我们公司地位还是很高的。

SQA还会不定期对开发团队进行个人的face to
face面对面一对一沟通，名字叫Audit，中文翻译过来类似叫审计。这种行为更针对"人"的评估，而不再是产品。因为产品的好坏决定于人的好坏。

## 4. 技术主管（Tech-Lead）

编程能力 ★★★★☆

业务认知 ★★★★★

沟通能力 ★★★★☆

管理能力 ★★★★

全局观 ★★★★

技术主管在我们公司往往就是一个项目的负责人。最主要的工作莫过于软件架构设计，客户需求沟通，技术难点解决和内部团队管理。

技术主管，名字便告诉了大家技术功底一定要很牛，在我们公司经常是一些工作了2-3年以上的软件工程师或者高级软件工程师担当。虽然技术很牛，不过实际上直接参与软件
开发的还是DEV（开发者），技术主管只是在比较高的一层面进行协调，所以直接代码编程很少。但是遇到了技术障碍DEV无法克服的时候，技术主管一定要及时站出来做一
个Problem solver。

技术主管的日常主要工作就是和客户沟通，熟悉需求，然后把业务需求转换成软件需求给DEV去做。所以技术主管对业务逻辑要相当的熟悉，在整个项目角色中，对业务最熟悉
的除了客户就是技术主管。所以技术主管起到了一个衔接的作用，沟通起了客户和开发，连接起了现实的业务需求和虚拟的软件实现。这一切，对技术主管的沟通能力的要求就很
高了。

软件团队不是一直和谐的，有时会出现某个模块的接口和另外一个模块的接口衔接不上，有时会出现一个人的工作被另外一个人的工作Block（中断）了，有时也会出现某个
DEV总是不买某个QA的账等等，所有的这一切，从技术到人本身，都在时时考验一个技术主管的管理水平。

## 5. 开发经理（SDM）

编程能力 ★★★☆

业务认知 ★★★★☆

沟通能力 ★★★★★

管理能力 ★★★★★

全局观 ★★★★★

软件开发经理是一般软件项目中执行层面上的最高职位了。其主要作用是项目的进度控制，客户高层沟通，甚至到项目预算控制。

软件开发经理的编程功底要看具体人而定，在我们公司软件开发经理一般都是技术出身，5-8年的工作经验或软件行业的资历。在具体的项目中，几乎不参与任何代码的编写和
设计工作。前期的项目计划（Project Plan），中期的项目进度管理和客户需求管理，到后期的项目交付，所有的工作都是软件开发经理和客户主要要沟通的东西。

业务方面，软件开发经理对业务认知的能力是非常强悍的，因为资历深的人对很多陌生的业务嗅觉和认知要比其他人强。不过在实际中，业务需求方面大部分工作给技术主管做了
，所以软件开发经理主要关注于项目总体，对细节不太关注了。

软件开发经理还有个重要的作用便是在软件项目过程中，积极地调动项目内外的资源。简单的说，把合适的人放在合适的位置上。当团队出现无法解决的问题时，软件开发经理会
想方设法从外部获取资源帮助团队渡过难关。

总的说了这么多，只是为了从宏观层面解释下这些角色的作用，目的是让新手大概的了解下这些角色的作用，以便今后在工作中将自己放在合适的角色以及和其他角色合作中心里
有个准备。


