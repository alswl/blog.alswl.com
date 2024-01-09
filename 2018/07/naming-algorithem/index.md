

![201807/bagua.png](https://e25ba8-log4d-c.dijingchao.com/upload_dropbox/201807/bagua.png)
<small>image from Wikipedia [八卦](https://zh.wikipedia.org/wiki/%E5%85%AB%E5%8D%A6)</small>

随着孩子预产期临近，我还有一个重要的任务没有完成：给孩子起一个名字。
这本来是个随性的任务，但是由于上一辈笃信某个算命先生的姓名测试算法，让这个任务难度倍增。
我根据一些古文取了不少名字，但是最后都败在姓名测试上面：得分不高。得分不高老一辈就要有说辞，
我自己就是一个活生生案例，曾用名得分不高，中考被逼换了名字，改头换面重新做人。

我根据韵律取的名字几乎都败在算分数上面，我得琢磨一下其中奥秘，提高取名效率，避免再出现差错。
不少网站都提供姓名测试算命，我且先看看上面的得分，研究一下规律：

- [姓名测试,姓名打评分,姓名算命,姓名分析,在线三才五格五行吉凶剖象](http://www.123cha.com/xm/)
- [姓名测试打分，根据周易三才五格取名法为您评测姓名-中华起名网](http://www.zhonghuaqiming.com/testname.aspx)
- [【姓名测试】姓名测试打分算命*姓名打分*姓名测试打分生辰八字 - 美国神婆星座网](https://www.meiguoshenpo.com/xingming/ceshi/)

每家网站都写得天花乱坠：易经、五格剖象法、五行起名、五格起名、三格数理。
这些都不用 Care，因为它们都是来自同一个算法：「三才五格」。

<!-- more -->

## 熊崎健翁的三才五格

我回想先生使用的算命方法，有这么几个特点：

- 跟我强调使用了「康熙字典」进行计算
- 给了我一个网址是 `.jp` 结尾，我当年上网计算之后，的确得到的数字和先生算计的一样，惊为天人

根据这两个线索，我很快挖掘到了
[姓名学 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%A7%93%E5%90%8D%E5%AD%A6)
。这里面就着重解释了日本人熊崎健翁的「三才五格」算法，

五格分别是天格、人格、地格、外格、总格，三才是天格、人格、地格的总称。
虽然三才五格看着挺像中国易经的概念，但其实是出口转内销的舶来品。
五格的具体解释如下：

- 天格：是先祖留传下来的，其数理对人影响不大。
- 地格：又称前运，影响人中年以前的活动力。
- 人格：又称主运，是整个姓名的中心点，影响人的一生命运。
- 总格：又称后运，影响人中年以后的命运。
- 外格：又称变格，影响人的社交能力、智慧等，其数理不用重点去看。

另外熊崎健翁还创造性的将五行引入，把这个模型做的更复杂。
不过评分的影响因子还是只有五格，单个字的五行并没有发挥直接的作用。
也有一些算命先生会刻意将单字的五行做成相生相克连贯起来，这样显得更有学问。

## 三才五格计算算法

这个算法的流程是这样：

- 计算每个汉字的笔画数
  - 姓名拆分为姓和名，尤其要注意单姓和复姓
  - 将简体姓和名转换为繁体姓和名
  - 将繁体姓和名映射为康熙字典中的姓和名
  - 将康熙字典中的姓和名的笔画数检出
- 根据笔画数计算五格（数字）
  - 天格：姓氏笔划再加一数即是天格数（若是复姓，将姓之笔划合计）
  - 人格：将姓氏与第一个名字相加即是人格数（若复姓双名，则姓氏的第二个字笔画加名的第一个字的笔画；
    复姓单名则姓氏的第二个字加名的笔画）
  - 地格：将第一个名字与第二个名字相加即是地格数（若是单名，将名字再加一数）
  - 外格：将名字最后一字加一数即是外格数
  - 总格：将姓与名相加即是总格数
- （可选）根据五格计算五行（这个五行对计算结果没有影响）
  - 尾数 1、2 于五行属木
  - 尾数 3、4 于五行属火
  - 尾数 5、6 于五行属土
  - 尾数 7、8 于五行属金
  - 尾数 9、10 于五行属水
- 根据笔画数得到解释
  - 计算规则见 [总格\_百度百科](https://baike.baidu.com/item/%E6%80%BB%E6%A0%BC)，
    其内容是列出 1-81 数字对应的情况，这个规则没有给出具体吉凶
- 根据解释得到吉凶等级
  - 123cha / 中华起名网 / 美国神婆都是根据这个解释给出一个大概吉凶，他们给吉凶有一些小差异
- 根据吉凶等级计算总分
  - 每家网站的算法有些差异，我估计算命先生的公式也应该有一些差异
  - 我自己根据对五格的解释，给出一个加权公式，跟几家算命网站进行了加权因子拟合

上述流程中，有两个给算命先生留出的调整空间：

- 根据解释推出吉凶
- 根据吉凶计算总分

根据解释推出吉凶，我研读了一下解释，比较倾向中华起名网和美国神婆的吉凶判断。
举例「旱苗逢雨」的解释，123cha 给出「(旱苗逢雨) 万物更新，调顺发达，恢弘泽世，繁荣富贵」吉。
中华起名网和美国神婆给出「（旱苗逢雨）：挽回家运的春成育数」和
「（旱苗逢雨）万物更新，调顺发达，恢弘泽世，繁荣富贵」大吉。
从解释的意象来看，我觉得应当作大吉。

第二个调整空间是根据吉凶计算总分。有了五格的吉凶，要给出百分制下面的总分，
这看上去需要一个加权公式。这个公式的设计决定最后得分多少。
我根据五格的定位设计了一份。

常见吉凶等级以及他们对应的得分，这个得分是我自行设计，从 100-0 依次排序：

- 大吉 100
- 吉 75
- \*半吉 62.5
- 平 50
- 凶 25
- 大凶 0

由于没有统一算法计算吉凶总分，我根据五格解释，设计了吉凶等级的加权因子：

- 天格：是先祖留传下来的，其数理对人影响不大。5%
- 地格：又称前运，影响人中年以前的活动力。20%
- 人格：又称主运，是整个姓名的中心点，影响人的一生命运。45%
- 总格：又称后运，影响人中年以后的命运。20%
- 外格：又称变格，影响人的社交能力、智慧等，其数理不用重点去看。10%

大功告成，我们拿几个姓名过来测算一下这个算法是否合理：

- 芮成钢总分：`100*0.05 + 62.5*0.2 + 100*0.45 + 62.5*0.2 + 100*0.1 = 85`
  - 123cha 72
  - 中华算命 92
  - 美国神婆 82
- 狄小天总分：`0*0.05 + 100*0.2 + 75*0.45 + 100*0.2 + 100*0.1 = 83.75`
  - 123cha 81
  - 中华算命 91
  - 美国神婆 85
- 狄二总分：`25*0.05 + 25*0.2 + 100*0.45 + 0*0.2 + 25*0.1 = 53.75`
  - 123cha 46
  - 中华算命 59
  - 美国神婆 65

通过最后的得分可以看到，三种算法的结果还是比较接近的。

## 工程实现

光实现了算法还没完，我还要有程序帮我做自动化计算。
名字的输入可以自行设计，用诗经、楚辞、古诗源等古文，然后导入程序计算得分。

为了工程实现，我需要准备如下数据：

- 简体汉字到繁体汉字的转换
- 繁体汉字到康熙字典中汉字比划数
- 根据笔画数计算出吉凶
- （可选）汉字对应的五行

经过一下午搜索，我终于将需要的数据准备好：

- [BYVoid/OpenCC: A project for conversion between Traditional and Simplified Chinese](https://github.com/BYVoid/OpenCC) 提供转换简繁体
- [breezyreeds/kangxi-strokecount: Lookup stroke count according to Kangxi radicals. 康熙字典筆劃數對照表](https://github.com/breezyreeds/kangxi-strokecount)
  提供笔画数
- 虽然 [总格\_百度百科](https://baike.baidu.com/item/%E6%80%BB%E6%A0%BC) 提供了解释，
  但是还是需要从相关网站爬取吉凶等级
- [EditPlus/Chinese.CTL at 26edd54bc26db36db8b3b17b4c670dc2953c78fe · Microshaoft/EditPlus](https://github.com/Microshaoft/EditPlus/blob/26edd54bc26db36db8b3b17b4c670dc2953c78fe/User/Chinese.CTL)
  提供了单个汉字的五行计算

## 最后

资深算命先生狄大师提醒大家，不管什么测字法都是玄学，玩玩就好，千万不要过于上心，
除非你家里有老人信这个，而你恰好又是一个孝子。

在一切准备就绪之后，我离出去当算命先生之差一个竹竿和墨镜了。
作为工程师，我当然会提供一个开放应用给大家用，请大家耐心等待我的小程序上架。
