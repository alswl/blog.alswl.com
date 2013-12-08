Title: Oracle PL/SQL编程规范
Author: alswl
Slug: oracle-pl-sql-coding-standards
Date: 2010-01-14 00:00:00
Tags: Database, Oracle, PL/SQL
Category: 综合技术

学习PL/SQL不可避免遇到规范的问题，这里转载一篇比较精的文章。

当然，各个公司和个人有自己的风格和规范，甚至Oracle官方的教程代码也没有完全遵守这些规则，这里只是一个推荐和介绍。

来源：[Oracle PL/SQL编程规范指南 -
51CTO.COM](http://database.51cto.com/art/200907/138973.htm)

更多参考：[SQL,PL/SQL编程规范 - PL/SQL -
IT民工杂谈](http://blog.chinaunix.net/u1/57759/showart_458439.html)

*****分割线，Google真汉子*****

## 一、PL/SQL编程规范之大小写

就像在SQL中一样，PL / SQL中是不区分大小写的。其一般准则如下：

关键字(`BEGIN`, `EXCEPTION`, `END`, `IF THEN ELSE`,`LOOP`, `END
LOOP`)、数据类型(`VARCHAR2`, `NUMBER`)、内部函数(`LEAST`,
`SUBSTR`)和用户定义的子程序(`procedures`, `functions`,`packages`)，使用大写。

变量名以及SQL中的列名和表名，使用小写。

## 二、PL/SQL编程规范之空白

空白（空行和空格）在PL/SQL中如同在SQL中一样重要，因为它是提高代码可读性的一个重要因素。换句话说，可以通过在代码中使用缩进来体现程序的逻辑结构。以下
是一些建议：

在等号或比较操作符的左右各留一个空格；

结构词（`DECLARE`, `BEGIN`, `EXCEPTION`, `END`,`IF and END IF`,` LOOP and END
LOOP`）居左排列。另外，结构中的嵌套结构要缩进三个空格（使用空格键，而不是Tab键）；

主要代码段之间用空行隔开；

把同一结构的不同逻辑部分分开写在独立的行，即使这个结构很短。例如，`IF`和`THEN`被放在同一行，而`ELSE `和`END IF`则放在独立的行。

## 三、PL/SQL编程规范之命名约定

使用以下前缀对于避免与关键字和表名列名相冲突是很有帮助的：

v_变量名

con_常量名

i_输入参数名，o_输出参数名，io_输入输出参数名

c_游标名 或者 游标名_cur

rc_ Ref Cursor名

r_Record名 或者 Record名_rec

FOR r_stud IN c_stud LOOP…

FOR stud_rec IN stud_cur LOOP

type_名称，名称_type (用户定义的类型)

t_表名，表名_tab （PL/SQL 表）

rec_Record名，Record名_rec （Record变量）

e_异常名 （用户定义的异常）

包的名称应该描述包内的存储过程和函数主要所完成的功能

存储过程的名称应该描述该存储过程所执行的动作

函数的名称应该描述所返回的变量

例如：

    
    
    PACKAGE student_admin
    --admin 后缀可能是用于表示管理功能.
    PROCEDURE remove_student (i_student_id IN student.studid%TYPE);
    FUNCTION student_enroll_count (i_student_id student.studid%TYPE)
    RETURN INTEGER;

## 四、PL/SQL编程规范之注释

PL/SQL中的注释如同SQL中的注释一样重要。他们应该解释程序的主要部分和所有关键的逻辑步骤。

使用单行注释(-)而不是多行注释(/*)。即使PL/SQL对这些注释做同样处理，这样在代码完成后进行调试也会容易些，因为你不能在多行注释中嵌入多行注释。换句
话说，单行注释代码中可以部分取消注释，而在多行注释代码中则不行。

## 五、其他的建议

对于PL/SQL中嵌入的SQL声明，使用相同的格式化指南来决定这些声明应该如何在代码块中出现

提供一个头部注释，用于说明代码块的用途并列出创建日期和作者名字。并且每个修订版都要有一行注释，包含作者名、日期和修订版描述。

例如：下面的这个示例体现了上述建议。请注意该示例还使用了等宽字体（Courier
New），因为每个字体占据同等宽度可以使格式化更加简便。等比例空格字体会隐藏空格使得行间对齐比较困难。多数文本和程序编辑器默认使用等宽字体。

    
    
    /********************************************************
    * 文件名：coursediscount01.sql  
    * 版本：1  
    * 用途：对于至少有一部分超过十个学生登记的课程给予折扣  
    * 参数：无  
    *  
    * 作者：s.tashi  时间：2000.1.1  
    * 修改者：y.sonam 时间：2000.2.1  
    * 描述：修正游标，添加缩进和注释。  
    ********************************************************/
    DECLARE
      -- C_DISCOUNT_COURSE 找出那些至少有一部分超过十个学生登记的课程  
      CURSOR c_discount_course IS
        SELECT DISTINCT course_no
          FROM section sect
         WHERE 10 <= (SELECT COUNT(*)
                        FROM enrollment enr
                       WHERE enr.section_id = sect.section_id);
      -- 费用超过 $2000.00的课程的折扣率  
      con_discount_2000 CONSTANT NUMBER := .90;
      -- 费用在$1001.00和$2000.00之间的课程的折扣率  
      con_discount_other CONSTANT NUMBER := .95;
      v_current_course_cost course.cost%TYPE;
      v_discount_all        NUMBER;
      e_update_is_problematic EXCEPTION;
    BEGIN
      -- 对于那些要打折的课程, 确定当前费用和新的费用  
      FOR r_discount_course in c_discount_course LOOP
        SELECT cost
          INTO v_current_course_cost
          FROM course
         WHERE course_no = r_discount_course.course_no;
        IF v_current_course_cost > 2000 THEN
          v_discount_all := con_discount_2000;
        ELSE
          IF v_current_course_cost > 1000 THEN
            v_discount_all := con_discount_other;
          ELSE
            v_discount_all := 1;
          END IF;
        END IF;
        BEGIN
          UPDATE course
             SET cost = cost * v_discount_all
           WHERE course_no = r_discount_course.course_no;
        EXCEPTION
          WHEN OTHERS THEN
            RAISE e_update_is_problematic;
        END; -- 更新记录的子代码块结束  
      END LOOP; -- 主循环结束  
      COMMIT;
    EXCEPTION
      WHEN e_update_is_problematic THEN
        -- 事务回滚  
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('There was a problem updating a course cost.');
      WHEN OTHERS THEN
        NULL;
    END;
    

&nbsp_place_holder;-EOF-

