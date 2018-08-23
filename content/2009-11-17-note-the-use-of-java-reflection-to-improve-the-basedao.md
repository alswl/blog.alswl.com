Title: Java笔记 使用反射来改进BaseDao
Author: alswl
Slug: note-the-use-of-java-reflection-to-improve-the-basedao
Date: 2009-11-17 00:00:00
Tags: Java, DAO, JavaSE, 贴吧, 重构
Category: Coding

## 关于反射

反射的定义（via [Wiki](http://zh.wikipedia.org/zh-cn/%E5%8F%8D%E5%B0%84_%28%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%29)）：在计算机科学中，反射是**指一种特定类型的计算机程序能够在运行时以一种依
赖于它的代码的抽象特性和它的运行时行为的方式被更改**的特性。用比喻来说，那种程式能够"**观察**"并且修改自己的行为。

Java中的反射示例如下：

    
    package dddspace.job.exercise1116;

public class Foo {

public void fun(String str) {

System.out.println(str);

}

}

    
    package dddspace.job.exercise1116;

import java.lang.reflect.InvocationTargetException;

import java.lang.reflect.Method;

public class ReflectionDemo {

public static void main(String[] args) throws SecurityException,

NoSuchMethodException, ClassNotFoundException, InstantiationException,

IllegalAccessException, IllegalArgumentException,

InvocationTargetException {

// 不使用反射

Foo foo = new Foo();

foo.fun("no reflection");

  
// 使用反射

String className = "dddspace.job.exercise1116.Foo";

String funName = "fun";

// 获取类名

Class cls = Class.forName(className);

// 创建Object实例

Object foo2 = cls.newInstance();

// 创建Method hello

Method method = cls.getMethod("fun", String.class);

// 使用反射来调用Method的invode方法，参数是目标对象+参数

method.invoke(foo, "use reflection");

}

}

## 原始BaseDao设计

我先阐述一下BaseDao的设计想法：BaseDao是一个**抽象类**，提供一系列Dao方法"**get()/getAll()/add()/update(
)/delete()/getCount()**"，通过**泛型匹配**的获取类，我取出一个方法来做示例。



    
    public int getCount()
    {
    	int count = 0;
    	Session session = null;
    	Transaction tx = null;
    	String Tstr = getClass().getSimpleName().substring (0,
    			getClass().getSimpleName().length() - 3);
    	String hql = "select count(*) from " + Tstr;
    	try {
    		session = HibernateSessionFactory.currentSession();
    		tx = session.beginTransaction();
    		Query query = session.createQuery(hql);
    		count = Integer.parseInt(query.uniqueResult().toString());
    		query = null;
    		tx.commit();
    	} catch (HibernateException e) {
    		if (tx != null) {
    			tx.rollback();
    		}
    		throw e;
    	} finally {
    		HibernateSessionFactory.closeSession();
    	}				
    	return count;
    }

其中有一段**dirty work**，就是TStr的获取，这段TStr是想从实现Dao类获取实体类的类型名称，也就是
从"TopicDao"获取"Topic"这个类型名称。整个BaseDao的泛型设计不错，但是在这一段上面存在一段dirty work，始终让我不爽。

## 重构BaseDao和TopicDao

我今天复习完抽象类/接口/反射这些内容，又在纸上画了一个模型，觉得用这种新方法解决会更好一点。

给抽象类BasoDao加入新的变量Class c，然后在TopicDao初始化时候对Class
c进行设置为Topic.class，这样就比原来的拼字符串好的多。耦合也显得漂亮了

    
    public abstract class BaseDAO<T> {
    	
    	protected Class c;
    	
    	private Logger logger = Logger.getLogger(this.getClass());
    	
    	/**
    	 * 根据某个Bean的beanId取出Bean
    	 * @param tId
    	 * @return Bean
    	 */
    	public T get(int tId)
    	{
    		T t=null;
    		Session session = null;
    		Transaction tx = null;
    		// 原始设计
    //		String Tstr = getClass().getSimpleName().substring (0,
    //				getClass().getSimpleName().length() - 3);
    		// 获取c的名称
    		String Tstr = c.getSimpleName();
    		String TstrId = Tstr+"Id";
    		String hql = "from " + Tstr + " where " +
    			TstrId.substring(0, 1).toLowerCase() + TstrId.substring(1) + " = ?";
    		try {
    			session = HibernateSessionFactory.currentSession();
    			tx = session.beginTransaction();
    			Query query = session.createQuery(hql);
    			query.setInteger(0,tId);
    			t = (T)query.uniqueResult();
    			query = null;
    			tx.commit();
    		} catch (HibernateException e) {
    			if (tx != null) {
    				tx.rollback();
    			}
    			throw e;
    		} finally {
    			HibernateSessionFactory.closeSession();
    		}		
    		return t;
    	}
    
    public class TopicDAO extends BaseDAO<Topic>{
    		
    	private Logger logger = Logger.getLogger(this.getClass());
    	/**
    	 * 根据froumId取出某一吧内的所有没被屏蔽的帖子
    	 * @param froumId
    	 * @return ArrayList<Topic> 
    	 * @throws HibernateException
    	 */
    	// 在构造函数中进行c的设置
    	public TopicDAO () {
    		c = Topic.class;
    	}
    	//doSomething
    }

这样完成之后，就完成了一次简单的重构，实现了**变化点分离**，而且不那么dirty。

本文的代码来源自PostBar项目。这里有[Google Code链接](http://code.google.com/p/postbar/)，v1.0.1的代码并没有上文的实现，本文中的修改还在trunk中。

