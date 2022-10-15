---
title: "「统计学」读书笔记"
author: "alswl"
slug: "statistics-note"
date: "2019-08-23T08:20:09+08:00"
tags: [""]
categories: [""]
draft: true
---

读书目的：

-   补齐基本的统计概念，在进行数据分析时候可以更 Reasonable
-   克服对数学公式的恐惧

感想：

年前做了一个项目 AIOps，其中两个功能是异常发现和趋势预测。
异常需要分析数据然后找出剧变数据，当时基于 ES 里面的内置包实现。
我研究了外部的 EGADS、Twitter Outlier 等论文，总感觉自己不得窍门，好多统计学属于看不懂，因此触发我看这本书。

看完之后，虽然没有打通任督二脉，但大致知道了基于统计方法论能够解决什么问题。
有稍微有些感知机器学习不少方法论是建立在统计学的基础之上的。只不过算力的增强让以前很多不可行的算法变得可行。
看完之后我对数学公式的恐惧感也降低了，可以比较熟练使用 Latex 来画公式了。
得到一个窍门，不要放过核心公式里面的每个字母，必须感知到整个公式里面，每一块是用来完成的目的的：促进还是抑制；
是否是收敛到某个值？是否还依赖外部某个公式？

为了读完此书还罚了 100 块钱 😂。


笔记：


-   链接
    -   [统计学 (豆瓣)](https://book.douban.com/subject/3516571/)
-   题材
    -   数学、统计学、教材
-   主题
    -   统计学研究范畴、工程使用、常见方法论
-   阅读对象
    -   大学生
-   阅读前问题
    -   统计学在使用中有什么应用 ✅
        -   描述数据、决策辅助、预测
    -   针对数据展开分析时候，有哪些特征来描述数据，使用哪些方法描述特征
        -   水平、差异、分布形状 ✅
        -   做判断的度量：置信区间、误差分析
-   阅读中问题
    -   自由度是啥
-   脉络
    -   统计学概览
        -   主要工作内容：收集、处理、分析、解释
        -   描述统计 Description Statistics
        -   推断统计 Inferential Statistics
        -   研究领域：几乎所有学科都需要的通用数据分析方法和数据分析语言
        -   变量和数据：变量 Variable、数据 Data、数值数据 Metric Variable、数值型数据 Metric Data、分类变量 Categorical
            Variable、定性变量 Qualitative Variable
        -   数据来源：样本 Sample，抽样方法：简单随机、分层抽样、系统抽样、整群抽样
    -   描述统计
        -   如何解读数据：关心什么特征、说明什么问题？
        -   描述数据：使用图标来直观解读数据
            -   频数分布表 Frequency Distribution，注意比例 Proportion 和 比率 Ratio，后者可以大于 1
            -   定性数据图
                -   条形图 Bar Chart
                -   帕累托图 Pareto Chart（条形图排序）
                -   饼图 Pie Chart
                -   环形图 Doughnt Chart
            -   定量数据图
                -   直方图 Histogram，使用矩形面积表示频数分布，
                -   茎叶图 Stem-and-leaf Plot，看原始数据方便（问题，难道不是看主子关系方便么？）
                -   箱线图 Box plot，p0 + p25 + p50 + p75 + p100，分析多组数据方便，比如考试成绩
                -   散点图 Scatter Diagram，一般会加上回归线
                -   雷达图 Radar Chart，散点图的二维坐标变换到多维
        -   描述数据：使用统计量
            -   水平，反应数据集中对外表现（作者：当前研究数据对外呈现）
                -   平均数 Mean
                -   中位数 Median 和分位数 Quartile
            -   差异，反应数据的离散程度（作者：数据内部一致性）
                -   极差 Range 和四分位差 Quartile Deviation（作者，敲黑板，Grafana 这个 Deviation 知道什么意思了吧）
                -   平均差 Mean Deviation，差异绝对值求和再平均
                -   方差 Variance，差异平方再平均
                -   标准差 Standard Deviation，$s^2$
                    -   标准分数 Standard Score $z_{i} = \frac{x_{i} - \bar{x}}{s}$
            -   分布形状，反应偏态和峰态（作者：详细描述数据内部）
                -   偏态 Skewness
                    -   $SK = \frac{n}{(n - 1)(n - 2)}\sum\left ( \frac{x - \bar{x}}{x} \right) ^3$
                -   峰态 Kurtosis
                    -   $K = \frac{n(n + 1)}{(n - 1)(n - 2)(n - 3)} \sum \left( \frac{x - \bar{x}}{x} \right) ^4 - \frac{3(n - 1)^2}{(n - 2)(n - 3))}$
        -   概率分布
            -   概率 Probability
                -   随机变量 Random Variable
                -   离散型随机变量 Discrete random variable / Continuous random variable
            -   期望值 Expected value，描述随机变量的集中程度（对外呈现）
                -   $\mu = E(X) = \sum_{i} { x_{i} P_{i}}$
            -   方差 Variance，描述随机变量的离散程度
                -   $\sigma^2 = D(X) = \sum_{i} { (x_{i} - \mu)^2 p_{i}}$
            -   离散型概率分布 Probability distribution
                -   二项分布 Binomial Distribution
                    -   只有成功和失败两种结果
                    -   每次实验结果概率相同
                    -   实验相互独立，并且可以重复
                -   泊松分布  Poisson Distribution
                    -   在一定时间段或空间或其他特定单位内某一事件出现的次数
                -   超几何分布
                    -   拿出不放回的二项分布
            -   连续型分布
                -   正态分布 Normal Distribution 
                    -   $X \sim N(\mu, \sigma^2)$
                    -   均值 $\mu$，体现在曲线水平位移
                    -   标准差 $\sigma$，体现在曲线的陡峭或者扁平
                    -   正态分布可以标准化，服从均值为 0，标准差为 1
                    -   图形化： [normal distribution - Wolfram|Alpha](https://www.wolframalpha.com/input/?i=normal%20distribution)
                    -   $\chi^2$ 分布 Chi-square distribution，$\chi^2(n)$ 的形状是不对称的，由 n 控制
                    -   $t$ 分布 t-distribution
                        -   用 t 表示样本均值经标准化后的新随机变量
                    -   $F$ 分布 F-distribution
                -   抽样分布 Sampling Distribution
                    -   总体参数 Parameter，对总体的概括性度量
                    -   统计量 Statistic，根据样本数据计算某个概括性度量
                    -   中心极限定理 Central limit theorey
                        -   从均值 $\mu$、方差 $\sigma^2$ 的总体中，抽取样本量为 $n$ 的随机样本，充分大（$n \geqslant 30$ )
                            样本均值分布近似服从均值为 $\mu$，方差为 $\frac{\sigma^2}{n}$
                        -   这位抽样统计理论埋下一个理论基础
                    -   比例 Proportion
                    -   标准误差 Standar error，样本统计量分布的标准差
                -   均匀分布 Uniform Distribution
                -   指数分布 Exponetial Distribution
    -   推断统计
        -   参数估计 Parameter estimation，用样本统计量估计总体的参数
            -   总体参数用 $\theta$，估计参数的统计量用 $\hat{\theta}$
            -   点估计 Point estimate
            -   区间估计 Interval estimate
            -   评价估计量
                -   无偏性 unbiasedness
                -   有效性 Efficiency
                -   一致性 Consistency
            -   区间估计，大样本服从正态分布，小样本的估计建立在大样本服从正态分布的基础上
            -   置信区间 Confidence Level，重复构造参数的置信区间中包含总体参数真值的次数所占的比例
                -   就这句话来看，抽象程度真的是高，描述真的是精准啊
        -   假设校验 Hypothesis test，先对总体参数提出一个假设值，再利用样本信息判断这一假设是否成立
            -   原假设（零假设 null hypothesis），想推翻的假设，使用 $H_{0}$ 表示
            -   备择假设 alternative hypothesis，想收集证据以支持的假设，使用 $H_{1}$ 或 $H_{a}$ 表示
            -   如何做决策
            -   第 I 类错误（原假设正确却拒绝了原假设）和第 II 类错误（原假设错误却没有拒绝原假设）
                -   （作者，前者是无知，后者是邪恶）
                -   不同场景的对 I II 选择不一样，是需要去平衡
            -   依据什么做决策？统计量、 P 值 Observed signification level（观察到的显著性水平）
    -   方差分析 Analysis of variance ANOVA：均值相等下面的统计方法
        -   从形式上看，方差分析是比较多个总体的均值是否相等，但本质上它所研究的是分类自变量对数值因变量的影响。
            -   （作者，这句话我琢磨十几遍，理解是方差分析是分析单个总体的内在情况，从而让外部可以对内部有度量来对比）
        -   误差分析：随机误差 Random error、组内误差 whtin-group error（残差）、处理误差 Treatment error
    -   模型：回归（Regression）中的一元线性回归
        -   因变量 Dependent variable（果）和自变量（因）Independent variable
        -   回归研究的课题：假定因变量与自变量之间有某种关系，并把这种关系用适当的数学模型表达出来，那么可以利用这一模型
            根据给定的自变量来预测因变量，这就是回归要解决的问题。
        -   回归直线，描述回归
            -   $\hat{y}_{i}=\hat{\beta}_{0}+\hat{\beta}_{1} x_{i}$
        -   最小二乘估计，使用垂直方向的离差平方估计参数 $\beta _{0}$ 和 $\beta _{1}$（其实就是观测值在 y 轴到回归线举例
            平方加总）
        -   拟合优度
            -   判定系数，对拟合优度的度量，总平方和 $SST=\sum\left(y_{i}-\overline{y}\right)^{2}$
        -   显著性校验，F 校验
        -   利用回归方程预测
            -   平均值的置信区间 Confidence Interval
                -   $\hat{y}_{0} \pm t_{\alpha / 2} s_{e} \sqrt{\frac{1}{n}+\frac{\left(x_{0}-\overline{x}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\overline{x}\right)^{2}}}$
            -   个别值的预测区间 Predication Interval
                -   $\hat{y}_{0} \pm t_{\alpha / 2} s_{e} \sqrt{1+\frac{1}{n}+\frac{\left(x_{0}-\overline{x}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\overline{x}\right)^{2}}}$
        -   校验方差齐性
            -   残差 Residual
    -   模型：回归（Regression）中的多元线性回归
        -   多元回归 Mutiple Regression，多元线性回归 Mutiple Linear Regression
            -   $y=\beta_{0}+\beta_{1} x_{1}+\beta_{2} x_{2}+\cdots+\beta_{k} x_{k}+\varepsilon$
        -   评估
            -   最小二乘估计 $Q=\sum\left(y_{i}-\hat{y}_{i}\right)^{2}=\sum\left(y_{i}-\hat{\beta}_{0}-\hat{\beta}_{1} x_{1}-\cdots-\hat{\beta}_{k} x_{k}\right)^{2}=\min$
            -   优度
                -   多重判定系数 Mutiple coefficence of determination
                -   估计误差标准 
        -   变量选择和逐步回归（作者，敲黑板，这里开始和数据处理相关了）
        -   变量选择，避免引入过多自变量（作者，降维是另外一回事）
            -   向前选择 Forward selection（加变量）、向后剔除 Backward elimination（减变量）、逐步回归 stepwise regression（加减一起迭代）
    -   模型：预测 - 时间序列
        -   （作者，居然在统计学这么「古老」的学科看到这么时髦的词汇，说明兜兜转转还是那一套）
        -    组成要素 Component：趋势 Trend、季节波动 Seaonal fluctuation，循环波动 Cyclical fluctuation、不规则波动
            irregular variance
        -   平滑预测法
            -   移动平均法 Moving average，非常朴素实现
                -   $F_{t+1}=\hat{Y}_{t}=\frac{Y_{t-k+1}+Y_{t-k+2}+\cdots+Y_{t-1}+Y_{t}}{k}$
            -   指数平滑法 Exponential smoothing，加权的移动平均法
                -   $F_{t+1}=\alpha Y_{t}+(1-\alpha) F_{t}$
            -   （作者，我之前看 AIOps 书籍，提出一些其他方案 ARIMA 等
        -   非线性预测
            -   指数曲线 exponential curve
                -   $\hat{Y}_{t}=b_{0} b_{1}^{t}$
            -   修正指数曲线 modified exponential curve
                -   $\hat{Y}_{t}=K+b_{0} b_{1}^{t}$
            -   Gompertz 曲线
            -   多阶曲线
        -   校验
    -   主成分分析和因子分析（降维）
        -   主成分分析 Principle component analysis
        -   因子分析 Factor analysis
    -   聚类
        -   聚类分析 Cluster Analysis：有的事先并不知道存在什么类别，完全按照反映对象特征的数据把对象进行分类
        -   判别分析 Discriminant analysis，事先有了某种分类标准之后，判定一个新的研究对象应该归属到哪一类别
        -   相似性度量
            -   欧氏距离、平方欧氏距离、Block 距离、Chebychev 距离、Minkovski 举例
        -   层次聚类
        -   K-means
    -   非参数校验（不依赖总体分布的校验）
-   给我带来的冲击和改变
    -   数据分析目的是为了寻找规律，而不是寻找支持。（困惑：科学不是讲究验证么）
    -   随着计算机算力提高，理解具体计算过程的价值，要低于理解计算背后理论和意图价值
    -   数学真是一门要求抽象能力高，描述精准的学科，怪不得很多问题最终转化成数学问题时候可以获得最终答案（比如 CAP）
    -   很多中文名称翻译不精准，比如残差 Winthin-group error（组内残差）和 Residual（预测值差）都叫残差
-   本文提到的其他书籍
    -   SKIP
-   作者
    -   贾俊平 中国人民大学统计学院副教授。研究方向：统计方法在经济各领域的应用、统计教学方式和方法。
-   评价
    -   优点
        -   给经管看的书，非工科书，很适合入门
        -   给出基于 Excel / SPSS 的实际操作，适合工程使用
        -   每章均给出术语表
        -   术语给出中英文对照
        -   挺应用的，好多实际场景的习题
    -   缺点
        -   缺少公式推倒（虽然我不定会看）
        -   缺少原理性阐述，比较偏应用（虽然我可能看不懂）

摘抄：

无。
