

本文来源：[Python天天美味(17) - open读写文件 - CoderZh的技术博客 - 博客园](http://www.cnblogs.com/coderzh/archive/2008/05/10/1191410.html)

「我本来想加上看到这篇文章的博客链接，结果粘贴时候发现了图片来源居然是cnblogs，这才反应过来这不是那个博客的原创。我不反对转载，看到的好文章我自己也会
收藏下来，转载能帮助更多需要的人，可是，至少加上人家原作者的地址呀……」-alswl

Python中文件操作可以通过open函数，这的确很像C语言中的fopen。通过open函数获取一个file
object，然后调用read()，write()等方法对文件进行读写操作。

## 1.open

使用open打开文件后一定要记得调用文件对象的close()方法。比如可以用try/finally语句来确保最后能关闭文件。


    file_object = open('thefile.txt')
    try:
        all_the_text = file_object.read( )
    finally:
        file_object.close( )

注：不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。

## 2.读文件

### 读文本文件


    input = open('data', 'r')
    #第二个参数默认为r
    input = open('data')

### 读二进制文件


    input = open('data', 'rb')

### 读取所有内容


    file_object = open('thefile.txt')
    try:
        all_the_text = file_object.read( )
    finally:
        file_object.close( )

### 读固定字节


    file_object = open('abinfile', 'rb')
    try:
     while True:
            chunk = file_object.read(100)
     if not chunk:
     break
            do_something_with(chunk)
    finally:
        file_object.close( )

### 读每行


    list_of_all_the_lines = file_object.readlines( )

如果文件是文本文件，还可以直接遍历文件对象获取每行：


    for line in file_object:
        process line

## 3.写文件

### 写文本文件


    output = open('data', 'w')

### 写二进制文件


    output = open('data', 'wb')

### 追加写文件


    output = open('data', 'w+')

### 写数据


    file_object = open('thefile.txt', 'w')
    file_object.write(all_the_text)
    file_object.close( )

### 写入多行


    file_object.writelines(list_of_text_strings)

注意，调用writelines写入多行在性能上会比使用write一次性写入要高。


