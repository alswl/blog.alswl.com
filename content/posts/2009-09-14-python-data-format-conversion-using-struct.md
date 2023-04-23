---
title: "Python中使用Struct数据格式转换"
author: "alswl"
slug: "python-data-format-conversion-using-struct"
date: "2009-09-14T00:00:00+08:00"
tags: ["python"]
categories: ["coding"]
---

本文来源：[Python模块学习 ---- struct 数据格式转换 - JGood的专栏 - CSDN博客](http://blog.csdn.net/JGood/archive/2009/06/22/4290158.aspx)

Python是一门非常简洁的语言，对于数据类型的表示，不像其他语言预定义了许多类型（如：在C#中，光整型就定义了8种），它只定义了六种基本类型：字符串，整数
，浮点数，元组，列表，字典。通过这六种数据类型，我们可以完成大部分工作。但当Python需要通过网络与其他的平台进行交互的时候，必须考虑到将这些数据类型与其
他平台或语言之间的类型进行互相转换问题。打个比方：C++写的客户端发送一个int型(4字节)变量的数据到
Python写的服务器，Python接收到表示这个整数的4个字节数据，怎么解析成Python认识的整数呢？
Python的标准模块struct就用来解决这个问题。

struct模块的内容不多，也不是太难，下面对其中最常用的方法进行介绍：

## struct.pack

struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组
）。其函数原型为：struct.pack(fmt, v1, v2, ...)，参数fmt是格式字符串，关于格式字符串的相关信息在[下面](http://bl
og.csdn.net/JGood/archive/2009/06/22/4290158.aspx#fmt)有所介绍。v1, v2,
...表示要转换的python值。下面的例子将两个整数转换为字符串（字节流）:


    import struct  
      
    a = 20  
    b = 400  

str = struct.pack("ii", a, b) #转换后的str虽然是字符串类型，但相当于其他语言中的字节流（字节数组），可以在网络上传输
print 'length:', len(str) print str print repr(str)

#---- result

#length: 8

# ----这里是乱码

#'x14x00x00x00x90x01x00x00'

格式符"i"表示转换为int，'ii'表示有两个int变量。进行转换后的结果长度为8个字节（int类型占用4个字节，两个int为8个字节），可以看到输出的结
果是乱码，因为结果是二进制数据，所以显示为乱码。可以使用python的内置函数repr来获取可识别的字符串，其中十六进制的 0x00000014,
0x00001009分别表示20和400。

## struct.unpack

struct.unpack做的工作刚好与struct.pack相反，用于将字节流转换成python数据类型。它的函数原型为：struct.unpack(fm
t, string)，该函数返回一个**元组**。 下面是一个简单的例子：


    str = struct.pack("ii", 20, 400)  
    a1, a2 = struct.unpack("ii", str)  
    print 'a1:', a1  
    print 'a2:', a2  
      
    #---- result:  
    #a1: 20  
    #a2: 400  

## struct.calcsize

struct.calcsize用于计算格式字符串所对应的结果的长度，如：struct.calcsize('ii')，返回8。因为两个int类型所占用的长度是
8个字节。

## struct.pack_into, struct.unpack_from

这两个函数在Python手册中有所介绍，但没有给出如何使用的例子。其实它们在实际应用中用的并不多。Google了很久，才找到一个例子，贴出来共享一下：


    import struct
    from ctypes import create_string_buffer

buf = create_string_buffer(12) print repr(buf.raw)

struct.pack_into("iii", buf, 0, 1, 2, -1) print repr(buf.raw)

print struct.unpack_from('iii', buf, 0)

#---- result

#'x00x00x00x00x00x00x00x00x00x00x00x00'

#'x01x00x00x00x02x00x00x00xffxffxffxff'

#(1, 2, -1)

## 关于格式字符串

**格式符**

**C语言类型**

**Python类型**

**注解**

x

pad byte

no value


c

char

string of length 1


b

signed char

integer


B

unsigned char

integer


?

_Bool

bool

(1)

h

short

integer


H

unsigned short

integer


i

int

integer


I

unsigned int

integer or long


l

long

integer


L

unsigned long

long


q

long long

long

(2)

Q

unsigned long long

long

(2)

f

float

float


d

double

float


s

char[]

string


p

char[]

string


P

void *

long


Notes:

1.The `'?'` conversion code corresponds to the `_Bool` type defined by C99. If
this type is not available, it is simulated using a `char`. In standard mode,
it is always represented by one byte.

New in version 2.6.

2.The `'q'` and `'Q'` conversion codes are available in native mode only if
the platform C compiler supports C `long long`, or, on Windows, `__int64`.
They are always available in standard modes.

New in version 2.2.

在Python手册中，给出了C语言中常用类型与Python类型对应的格式符：具体内容请参考Python手册
[struct](http://docs.python.org/library/struct.html#module-struct) 模块

