---
title: "再读《重构》"
author: "alswl"
slug: "refactory"
date: "2012-02-05T00:00:00+08:00"
tags: ["综合技术", "读书笔记"]
categories: ["coding"]
---

Martin Fowler 的「[重构-改善既有代码的设计](http://book.douban.com/subject/1229923/)」这本书，是我大学老师推荐给我的。
当时我在撰写代码过程中，发现当代码量到某个数量级时候（1000+行），
就会逐渐失去对代码的控制能力。
昆哥推荐了两本书「[UML 和模式应用](http://book.douban.com/subject/1792387/)」和「重构」这本书。

![Refactory](/images/upload_dropbox/201202/s1669771_l.jpg)

这本书是2年前购买的，可惜以我当时的代码感知和撰写能力，看起来颇为吃力。 半途就看得云里雾里而中断了。最近我又重新拾起这本书，
将书中所写的境况与我这两年多来遇到的问题相互印证，才感受到这本经典的力量。

Martin 其人：

    
>   ThoughtWorks 的首席科学家，当今世界软件开发领域最具影响力的五位大师之一。
>   他在 UML 推广普及、领域建模、企业应用开发和敏捷方法等方面建树卓著，被称为软件开发的教父。

大学时候有段时间我对 Martin 的敏捷非常痴迷。现在对技术的选择没以前那么冲动了， 但是毫不妨碍我对 Martin 的敬仰之情。

## 1. 重构原则

### 1.1. 重构的定义

    
>   对软件内部结构的一种调整，目的是在不改变"软件之可察行为"前提下，提高其可理解性，降低其修改成本。

重构就是在代码写好之后改进它的设计。

*   重构和添加新功能并不冲突，但是当开发者身份在两者之间切换时候，不能混淆在一起。

### 1.2. 重构的意义

*   优秀设计的根本是：消除重复部分！（DRY = Don't repeat yourself）
*   重构让代码更清晰，更容易理解
*   清晰的代码可以更方便的找到 bug ，重构可以写出更强健的代码
*   良好的设计可以在长远时间上提高开发速度

### 1.3. 重构的时间

*    随时进行重构（在我看来，重构更是一种开发的习惯）
*    事不过三，代码重复不要超过三次（否则就要"抽"出来）
*    添加功能时候并一一重构（个人理解是，添加新功能之前，分析并重构，从而更方便添加新功能）
*    修补错误时
*    Code Review 时

### 1.4. 重构和开发进度

重构的意义之一也是提高开发进度。杀手锏是"不要告诉经理"。

### 1.5. 重构的难题

*    数据层（数据模型）的变更压力
*    修改接口
*    那些难以通过重构改变的设计改动
*    代码不能运行
*    项目期限压力 Deadline

### 1.6. 重构与设计

*   编程不是机械的开发，（软件开发是艺术行为！）
*   设计和重构的平衡（预先设计的难度和重构灵活性的平衡）

### 1.7. 重构与性能

*   重构确实会在短期内降低代码执行效率，但优化阶段是可以调整的，而且调整会更容易。
*   提前优化是万恶之源

### 1.8. 那些Bad Smell

*    重复的代码（这才是真正万恶之源，鄙视一切Ctrl+C/P）
*    过长函数，会导致责任不明确/难以切割/难以理解等一系列问题
*    过大类，职责不明确，垃圾滋生地
*    过长参数列（面向对象不是说说而已）
*    发散式变化，一个类会响应多种需求而被修改
*    散弹式修改（其实就是没有封装变化处，由于一个需求，多处需要被修改）
*    依赖情节（一个类对其他类过多的依赖）
*    数据泥团（如果数据有意义，就将结构数据变成对象）
*    Type code，使用 Class 替代
*    `switch`，少用，考虑多态
*    过多平行的类，使用类继承并联起来
*    冗余类，去除它
*    夸夸其谈的未来性（Matin 的文字，侯俊杰的翻译真是…出彩…）
*    临时值域，封装它
*    过度耦合的消息链，使用真正需要的函数和对象，而不要依赖于消息链
*    过度的 Deleate
*    过度使用其他类 `private` 值域
*    重复作用的类
*    不完美的类库，（类库老了，使用者也没办法阿）
*    纯数据类（类需要行为）
*    不纯粹的继承（拒绝父类的接口的类）
*    过多注释，注释多了，就说明代码不清楚了

### 1.9. 从测试开始

无测试，无重构，只依赖手工测试，重构时候人会崩溃的。

*   重构的保真就是自动化测试（如果真的要无聊的手工测试，我也不反对）
*   单元测试
*   功能测试

### 1.10. Kent Back说

    
>   如果我纯粹为今天工作，明天我将完全无法工作。

间接层的价值：

*   允许逻辑共享  
*   分开解释"意图"和"实现"  
*   将变化加以隔离  
*   将条件逻辑加以编码

>   计算机科学是这样一门学科：它相信所有问题都可以通过一个间接层来解决。
>
>   --Dennis DeBruler

我相信，撰写代码时候不仅仅考虑当下功能，要考虑到有可能出现的情况，
在可能的平衡下面，为将来的扩展做好准备。（也许不仅仅是自己的明天，
还要考虑团队成员的今天工作内容）

## 2. 重构名录

### 2.1. 重新组织函数

Extract Method（提炼函数）

>   将一段独立的，不依赖上下文的代码组织并独立出来。

Inline Method（将函数内联化）

>   当函数内部代码简短而容易理解时候，去除这个非必要的间接层。

Inline Temp（将临时变量内联化）

>   去除只被赋值一次的临时变量。（当有意义时候，应该保留）

Replace Temp with Query（以查询取代临时变量）

>   将临时变量提取到一个独立函数，并将原来变量引用替换为函数调用。 （我还是担心性能的问题，另外将临时变量限定在一个段落中，可以避免额外的引用）

Introduce Explainning Variable（引入解释性变量）

>   将复杂表达式的结果放入临时变量，并用变量名来解释表达式用途。 （自注释代码的表现）

Split Temporary Variable（剖析临时变量）

>   除了循环变量和临时集合变量，临时变量赋值不能超过一次。

Remove Assignments to Parameters（移除对参数的赋值动作）

>   不对函数参数进行赋值动作，如果要赋值，创建一个新的临时变量。

Replace Method with Method Object（以函数对象取代函数）

>   把函数变成对象，再把临时变量变成对象值域。该方法在分解函数时候常用。 （Martin 对小型函数特别迷恋，我认为这个方法更应该用在有逻辑意义的方法上面）

Substitute Algorithm（替换算法）

>   用更清晰的算法。 （码农都知道）

### 2.2. 在对象之间搬移特性

（面向对象编程原则之一就是职责归属，搬移其实也就意味着职责重新规划）

Move Method（搬移函数）

>   将函数移动到被最多次调用的类里面去。 （往往在逻辑意义上，这个函数就应该归属于这个类）

Move Field（搬移值域）

>   将值域移动到被最多次调用的类里面去。

Extract Class（提炼类）

>   将开发过程中逐渐变得臃肿的类拆分成数个类，形成清楚的抽象，明确的职责。

Inline Class（将类内联化）

>   将不再担任足够职责的类搬到另外一个类中，并移除这个原始类。

Hide Delegate（隐藏委托关系）

>   将直接调用变成间接，在中间添加一层，从而从容面对变更，隔离变化。 （"哪里变化，封装哪里"这是设计模式的一个经典原则）

Remove Middle Man（移除中间人）

>   和Hide Delegate相反，移除做了过多简单委托的类。 （应该Hide Delegate需要加入成本，多维护一层，这需要控制一种平衡）

Introduce Foreign Method（引入外加函数）

>   当类无法进行修改时候，使用静态函数接受这种类型的类实例，

Introduce Local Extenstion（引入本地扩展）

>   使用子类继承/Wrapper 类来实现额外的函数。

### 2.3. 重新组织数据

Self Encapsulate Field（自封装值域）

>   使用getter/setter。 （个人觉得这样很繁琐，.net 中的属性方式处理的不错）

Replace Date Value with Object （以对象取代数据值）

>   当数据项有额外的数据和行为时候，将它变成一个类

Change Value to Reference（将实值对象改为引用对象）

>   有一些类型，比如日期、星期，不需要保存太多副本。

Change Reference to Value（将引用对象改为实值对象）

>   和楼上相反的情况，引用会带来复杂的内存分配，在分布式系统中，实值对象特别有用。

Replace Array with Object（以对象取代数组）

>   不应该将不同的元素存放到数组中，应该使用值域。

Duplicate Observed Data（复制被监视数据）

>   通过观察者模式，将业务数据和 GUI 数据进行同步控制

Change Unidirectional Association to Bidirectional（将单向关联改为双向）

>   使用双向连接，从而能让两个类能互相使用对方特性。

Change Bidirectional Assicuation to Unidirectional（将双向关联改为单向）

>   当一个类不再需要另外一个类特性时候作修改。

Replace Magic Number with Symbolic Constant（以符号常量/字面常量取代魔法数）

>   使用有意义的名称，比如pi, gravity。

Encapsulate Field（封装值域）

>   使用getter/setter。

Encapsulate Collection（封装集群）

>   避免直接修改容器对象，而是封装出类方法来修改。将变化控制在既有方法内。

Replace Record with Data Class（以数据类取代记录）

>   将传统编程中的结构体转换为数据类。

Replace Type Code with Class（以类别取代型别码）

>   使用类型集合类来替换型别码。

Replace Type Code with Subclass（以子类取代型别码）

>   使用多态来替换型别码，发挥面向对象编程的优势。 （小心处理 ORM 映射）

Replace Type Code with State/Strategy（以State/Strategy取代型别码）

>   使用State/Strategy模式来因对type code会发生变化的情况。 将状态类作为父类，再进行继承。

Replace Subclass with Fields（以值域取代子类）

>   当子类的差异仅仅体现在返回常量数据的函数上时候，进行这样的替换。

### 2.4. 简化条件表达式

简化的核心思想，是将过程式的 `if` / `else` 替换为面向对象的多态。

Decompose Conditional（分解条件式）

>   将复杂的条件式提炼为独立函数。

Consolidate Conditional Expression（合并条件式）

>   将多个条件式判断提炼成一个独立函数。这和上面的分解条件式都需要一个前提： 这几个条件式是要有逻辑关联的。

Consolidate Duplicate Conditional Fragments（合并重复的条件判断）

>   将所有分支里面都拥有的代码提炼到分支判断之后运行。

Remove Control Flag（移除控制标志）

>   使用 break/return 取代控制标记。单一出口，多出口。控制标记让程序接口看上去混乱。

Replace Nested Conditional with Guard Clauses（以卫语句取代嵌套条件式）

>   保留正常情况下面下的顺序执行，提前对非正常情况进行单独检查并返回。 （我更倾向于使用 Exception）

Replace Conditional with Polymorphism（以多态取代条件式）

>   将条件式的每个分支放入一个Subclass 内覆写函数中，然后将原始函数生命为抽象函数。
（这个方法之前的 5 种重构手段是代码小手段，引入多态才能充分发挥 OOP 优势）

Introduce Null Object（引入 Null 对象）

>   将无效值替换为Null Object，从而可以让程序正常运行。 （这好象是一种 Hack 方法，我倾向使用 Exception，作者的用以可能是通过 Null 来减少判断代码）

Introduce Assertion（引入断言）

>   通过断言来发现程序错误，实际使用中，可以配合 Debug Mode 使用。

### 2.5. 简化函数调用

Rename Method（重命名函数）

>   A good name is better than a line of comment.

Add Parameter（添加参数）

>   你没看错，就是添加参数。 （啊？Matin老师，不带这么水的阿）

Remove Parameter（移除参数）

>   不要就丢掉。

Separate Query from Modifier（将查询参数和修改参数分离）

>   将一个即查询状态又修改状态的函数分离开来，职责分离清楚。 （我以前很喜欢写多面手函数～）

Parameterize Method（令函数携带参数）

>   同一逻辑功能函数，通过重载接受不同参数。而不要建立多个同样的函数。

Replace Parameter with Explicit Methods（以明确函数取代参数）

>   将单一函数分解为多个函数从而去掉参数，前提是这几个函数的逻辑功能区别较大。

Preserve Whole Object（保持对象完整）

>   传递完整的对象，取代几个参数的传递。

Replace Parameter with Methods（以函数取代参数）

>   如果目标函数需要的是几个参数操作的结果，就直接传递这个结果，而不是数个参数。

Introduce Parameter Object(引入参数对象)

>   当几个参数经常同时出现，就封装他们。 （他们之间往往就有逻辑关系）

Remove Setting Method（移除设值函数）

>   如果类的某个值域初始化后不再改变，就去掉它的 setting 方法。 （我理解为原则："减少疑惑，保持唯一"）

Hide Method（隐藏某个函数）

>   使用 private 标记未被其他类调用的方法。

Replace Constructor with Factory Method（以工厂函数取代构造函数）

>   引入工厂模式。

Encapsulate Downcast（封装向下转型动作）

>   当知道什么类型时候，将其封装在产生函数里面，减少引用者的困扰。

Replace Error Code with Exception（以异常取代错误码）

>   如其名。 （关于异常使用的时机，抛出的方式，捕捉的粒度，我困惑了很久。 最后的总结的经验是：在什么层级处理并且仅处理该层级的异常。等有时间详细成文送出）

Replace Exception with Test（以测试取代异常）

>   异常不是条件判断。

### 2.6. 处理概括关系

关于 OOP 继承的那些事儿。

Pull Up Field（值域上移）

>   子类重复的值域放到父类去。 （其实还是基于责任归属的问题）

Pull Up Method（函数上移）

>   子类中重复函数移到父类。

Pull Up Construction Body（构造函数本体上移）

>   共用的构造函数片段上移。

Push Down Method（函数下移）

>   将父类中近被某个子类调用的函数下移。

Push Down Field（值域下移）

>   同上。

Extract Subclass（提炼子类）

>   当某个类只有部分特性被用到，就需要提取出子类。

Extract Superclass（提炼超类）

>   和上面相反。

Extract Interface（提炼接口）

>   将相同的子集提取接口。

Collapse hierarchy（折叠继承体系）

>   父类和子类并无太大区别时候，合体吧亲。

From Template Mehod（塑造模板函数）

>   将子类的同功能不同实现函数上移到父类，并在子类提供同名不同实现被调用的子函数。

Replace Inheritance with Delegation（以委托取代继承）

>   将父类变成一个值域，在调用这个值域的方法。is-a -> has-a （继承太多就会出问题）

Replace Delegation with Inheritance（以继承取代委托）

>   和上面相反的应用，当子类和父类出现明显的继承关系时候使用。

### 2.7. 大型重构

这一章讲的内容有点高屋建瓴，这里就不概括了，建议读原文。

*   Tease Apart Inheritance（梳理并分解继承体系）
*   Convert Procedural Design to Objects（将过程化设计转化为对象设计）
*   Separate Domain from Presentation（将领域和表述/显示分离）
*   Extract hierarchy（提炼继承体系）

少年，Coding 时候重构你的代码吧！
