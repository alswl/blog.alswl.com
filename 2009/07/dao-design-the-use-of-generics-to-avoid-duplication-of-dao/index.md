

DAO的全称是Data Access Object数据访问接口。数据访问：顾名思义就是与数据库打交道。夹在业务逻辑与数据库资源中间。

我大二时候写的一个小型管理系统，那时候老师开始强调分层和MVC的思想，当时我将DAO层分了开来，把所有与数据库的交互操作封装成对应的DAO类，这样最大的好处
是实现了封装和隔离，方便系统的迁移和重构。

分层、封装、接口化是一种基本的解决思路，无论是TCP/IP协议族，还是软件工程，都是很值得使用的方案。

那么接下来的问题就是DAO类的设计，我当时遇到的问题就是DAO类之间存在大量的冗余代码，用敏捷的角度来思考，这绝对是不允许存在的。

讲相同的方法抽象出来，这也是最常见的解决方案，最简单的例子就是函数的产生，其实也是对程序的一种抽象和提炼，避免冗余，达到复用效果。

在Java1.5出来之前，用Object来操作对象，实现方法复用，就可以达到上面的目的，但是，存在类型安全的问题。Java1.5提出了泛型的概念，类似与C+
+中的Template，Java运行环境帮助会检查类型的安全。

这里有一篇IBM资料库的文章，详细阐述了泛型在DAO设计的使用「不要重复DAO」<[猛击这里打开](http://www.ibm.com/developerworks/cn/java/j-genericdao.html)>，作者[PerMellqvist (http://www.ibm.com/developerworks/cn/java/j-genericdao.html#author)
([per@mellqvist.name](mailto:per@mellqvist.name?subject=%E4%B8%8D%E8%A6%81%E9%87%8D%E5%A4%8D%20DAO%EF%BC%81)), 系统架构师, 自由作家

我的贴吧里面DAO最后的UML类图设计如下：

[![DAO_UML](/images/upload_dropbox/200907/DAO_UML-254x300.jpg)](../../static/images/upload_dropbox/200907/DAO_UML.JPG)


