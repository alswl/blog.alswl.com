---
title: "Python 的类型系统"
author: "alswl"
slug: "type-safe-python"
date: "2020-06-23T17:54:00+08:00"
tags: ["python"]
categories: ["coding"]
---

![wall](../../static/images/upload_dropbox/202006/wall.png)
<small>image from pixabay.com</small>

静态类型正在逐渐成为潮流，
2010 年之后诞生的几门语言 Go、Rust、TypeScript 等都走了静态类型路线。
过往流行的一些动态语言（Python、PHP、JavaScript）也在积极引入语言新特性（Type Hint、TypeScript）对静态类型增强。

我曾使用 Python 开发规模较大的项目，感受过动态语言在工程规模变大时候带来的困难：
在重构阶段代码回归成本异常之高，很多历史代码不敢动。
后来技术栈转到 Java，被类型系统怀抱让人产生安全感。

最近一年在一个面向稳定性的运维系统耕耘。系统选型之初使用了 Python。
我在项目中力推了 Python 3.7，并大规模使用了 Python 的类型系统来降低潜在风险。

追根溯源，我花了一些时间了解 Python 在类型系统的设计和实现，
本文以 PEP 提案介绍一下 Python 在类型系统上面走过的路。

<!-- more -->

## 类型系统

谈类型系统之前，要厘定两个概念，动态语言和动态类型。

动态语言（Dynamic Programming Language）则是指程序在运行时可以改变结构。
这个结构可以包含函数、对象、变量类型、程序结构。
动态类型是类型系统（Type System）其中一类，即程序在运行期间可以修改变量类型。
另外一种是静态类型：在编译期就决定了变量类型，运行期不允许发生变化。
类型系统还有一种分法是强类型和弱类型，强类型是指禁止类型不匹配的指令，弱类型反之。

动态语言和动态类型这两个概念切入点不一样，
Python 是一门动态语言，也是动态类型语言，还是强类型的动态类型。
这篇文章主要讨论 Python 语言的类型系统，不会涉及动态语言特性。

## 类型安全之路

行业里面一直有一个争论：动态类型和静态类型哪一种更强大。
静态类型的支持者认为三个方面具备优势：性能、错误发现、高效重构。
静态类型通过编译期决定具体类型可以显著的提高运行期效率；
编译期就能够发现错误，在工程规模逐步变大时候尤其明显；
类型系统可以帮助 IDE 提示，高效重构。
动态类型的支持者则认为分析代码会更简单，减少出错机会，写起来也更为快速。

Python 开发者们并非没有看到这个痛点，
一系列 PEP 提案应运而生。
在保留 Python 动态类型系统优势前提，通过语法、特性增强，将类型系统引入 Python。

Python 在 2014 年即提出了 PEP 484，随后提出一个精粹版 PEP 483（The Theory of Type Hints），
其工程实现 [typing](https://docs.python.org/3/library/typing.html) 模块在 3.5 发布。
经过 PEP 484，PEP 526，PEP 544，PEP 586，PEP 589，PEP 591 的多次版本迭代，Python 的类型系统已经很丰富。
甚至包含了比如 Structural Subtyping 以及 Literal Typing 这边相对罕见的特性。

### PEP 483 - 核心概念

[PEP 483](https://www.python.org/dev/peps/pep-0483/) 在 2014 年 12 月发布，
是 Guido 起笔的核心概念版，简明扼要的写清楚 Python 的类型系统建设方向、边界、要和不要。

PEP 483 没有谈具体工程实现，提纲挈领地讲了一下 Python 类型系统如何对外呈现。
厘定 Type / Class 差别，前者是语法分析概念，后者是运行时概念。
在这个定义下面 Class 都是一个 Type，但 Type 未必是 Class。
举例 `Union[str, int]` 是 Type 但并不是 Class。

PEP 483 还介绍内建基础类型：`Any` / `Unison` / `Optional` / `Tuple` / `Callable`，这些基础类型支撑上游丰富变化。

静态类型系统最大的诟病是不够灵活，Go 语言现在还没有实现泛型。
PEP 483 介绍了 Python Generic types 泛型使用方法，
形式如下：

```python
S = TypeVar('S', str, bytes)

def longest(first: S, second: S) -> S:
    return first if len(first) >= len(second) else second
```

最后，PEP 483 还提了一些重要的小特性：

- 别称 Alias
- 前置引用 Farward Reference（在定义类方法注解中使用定义类），eg.：解决二叉树 Node 节点中需要引用 Node 问题
- covariance contravariant 协变逆变
- 使用注释标记类型
- 转型 Cast

PEP 483 的实现，主要依赖了 [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)
这个提案。PEP 3107 介绍 function 注解使用。比如， `func(a: a1, b: b1) -> r1`
这段代码，
其中冒号后面的描述符记录会到 func 的 `__annotations__` 变量中。

PEP 3107 效果展示如下，可以清晰看到函数变量存放：

```python
def add(x: int, y: int) -> int:
    return x + y

add.__annotations__
# {'x': int, 'y': int, 'return': int}
```

PS：现在 Python 有了 Decorator 装饰器 / Annotation 注解，其中 Annotation 的设计还和 Java 的 Annotation 同名，一锅粥。

### PEP 484 - Type Hints 核心

[PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
在 PEP 483 基础上完整讲述 Python 类型系统如何设计，如何使用，细节如何（typing 模块）

这篇提案开宗明义地点出：

> Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory,
> even by convention.

一句话断绝了 Python 在语言级别进化到静态系统的可能。

提案除了 PEP 483 已经讲解的特性，还有以下吸引我的点：

- 允许通过 Stub Files 为已经存在的库添加类型描述。具体是使用 Python 文件对应的 `.pyi` 文件描述 Python 代码的带类型签名。
  这个方案和 TS 的 `@types` 文件有异曲同工之妙。
- 允许使用 `@overload` 进行类型重载，这也是活久见，Python 居然可以（在某种意义上）支持重载了。
- 介绍了 typing 实现细节，比如使用 abs（Abstract Base Class）构建常见类型的 interface，包括 `Sized` / `Iterable` 这些基础接口。
  我个人认为这个工作量是其实挺大，是给已有的类进行一次依赖梳理。
- 介绍了 Python 向后（Python 2）兼容方法，有这么几种策略：
  使用 decorator（`@typehints(foo=str, returns=str)`）、comments、Stub files、Docstring

### PEP 526 - 变量也安排上了

[PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
核心提案是给变量加上 Type Hints 支持。

和 `function annotation` 类似，也是通过注解方式存放。
差异是并不是给实例添加一个 `__annotations__` 成员，而是将变量的 annotations 信息存放在上下文变量 `__annotations__` 之中。
这个其实也比较好理解：定义一个变量类型时候，这个变量还没有初始化。

我写一段 Demo 展示一下：

```python
from typing import List
users: List[int]

# print(__annotations__)
# {'users': typing.List[int]}
```

可以看到，上述 Demo 效果是在上下文变量创建了一个 `users`，但这个 `users` 其实并不存在，只是定义了类型，
如果运行 `print(users)` 会抛出 `NameError: name 'users' is not defined`。

观察字节码会更清晰：

```
 L.   1         0  SETUP_ANNOTATIONS

 L.   1         2  LOAD_CONST               0
                4  LOAD_CONST               ('List',)
                6  IMPORT_NAME              typing
                8  IMPORT_FROM              List
               10  STORE_NAME               List
               12  POP_TOP

 L.   3        14  LOAD_NAME                List
               16  LOAD_NAME                int
               18  BINARY_SUBSCR
               20  LOAD_NAME                __annotations__
               22  LOAD_STR                 'users'
               24  STORE_SUBSCR
               26  LOAD_CONST               None
               28  RETURN_VALUE
```

可以清晰看到，并没有创建一个名为 users 的变量，而是使用了 `__annotations__` 变量。
注：Python 存储变量使用 opcode 是 `STORE_NAME`。

PS：本提案中有不少被否决的提案，挺有趣的，社区提出了很多奇淫巧计。
可以看出社区决策的慎重，存量系统升级的难度。

### PEP 544 - Nominal Subtyping vs Structural Subtyping

PEP 484 里面类型系统讨论的是 Nominal Subtyping，
这个 [PEP 544 -- Protocols: Structural subtyping (static duck typing)](https://www.python.org/dev/peps/pep-0544/)
则是提出了Structural Subtyping。
如果非要翻译，我觉得可以称为具名子类型 / 同构子类型。
注意，也有人将 Structural Subtyping 称之为 Duck Typing，其实这两者不相同，具体可以见
[Duck typing / Comparison with other type systems](https://en.wikipedia.org/wiki/Duck_typing#Structural_type_systems)。

Nominal Subtyping 是指按字面量匹配类型，而 Structural Subtyping 则是按照结构（行为）进行匹配，
比如 Go 的 Type 就是 Structural Subtyping 实现。

这里写个简单 Demo 展示一下后者：

```python
from typing import Iterator, Iterable

class Bucket:
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result: int = collect(Bucket())  # Passes type check

```

代码中定义了 Bucket 这种类型，并且提供了两个类成员。这两个类成员刚好是 Interator 的定义。
那么在实际使用中，就可以使用 Bucket 替换 Iterable。

### PEP 586 / PEP 589 / PEP 591 持续增强

[PEP 586 -- Literal Types](https://www.python.org/dev/peps/pep-0586/)
在 Python 3.8 实现，支持了字面量作为类型使用。
比如 `Literal[4]`，举一个更有语义的例子 `Literal['GREEN']`。

我第一反应这和 Scala 里面的 Symbol 非常像，Scala 中写法是 `Symbol("GREEN")`。
这个特性使用挺学院派，很容易在 DSL 里面写的天花乱坠。
Scala 官方有说过可能在未来移除 Symbol 特性，建议直接使用常量替代。

[PEP 589 -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys](https://www.python.org/dev/peps/pep-0589/)
给 Dict 增加 key 的 Type，继承 `TypedDict`。

[PEP 591 -- Adding a final qualifier to typing](https://www.python.org/dev/peps/pep-0591/)
增加 `final` / `Final` 两个概念，前者是装饰器，后者是注解，标注该类 / 函数 / 变量无法修改

至此，Python 3.8 已经具备我们日常需要的类型系统特性（非运行时 😂）。

## 总结

遗憾的是，`typing` 模块在文档鲜明的标注：

> The Python runtime does not enforce function and variable type annotations. They can be used by third party tools
> such as type checkers, IDEs, linters, etc.

即：Python 运行时（Intercepter / Code Evaluator）并不支持函数和变量的类型装饰符。
这些装饰符只能由第三方工具检查，比如类型检查器、IDE、静态、Linter。

这个信息说明了 Python 在类型安全上尝试的局限性。所有的限制、约束都不会发生在运行时，
想要从类型系统中收获工程上面的价值，只能借助第三方工具。

诚然，Python 社区在竭力向类型系统靠拢，但是这种非语言级别 Runtime 的支持，到底能走多远呢？
Python 缺少金主爸爸，干爹 Red Hat 投入资源也有限。连社区从 Python 2 切换到 Python 3 都还没走完，为何？
投入产出比太低，新特性缺乏足够的吸引力，替代品太多。

另一方面，看看竞对们：
动态语言在往静态语言靠拢，而静态语言也在不断吸收动态语言的特性。比如 Java 14 里面的 REPL（Read-Eval-Print-Loop），
Kotlin / Scala 等语言的类型推断（Type Inference）。
也许这种演进方式更能够让用户接受吧。

## 参考

- [typing — Support for type hints — Python 3.8.3 documentation](https://docs.python.org/3/library/typing.html)
- [PEP 483 -- The Theory of Type Hints | Python.org](https://www.python.org/dev/peps/pep-0483/#type-variables)
- [PEP 484 -- Type Hints | Python.org](https://www.python.org/dev/peps/pep-0484/#abstract)
- [the state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/)
