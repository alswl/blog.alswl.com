

这个想法一直就有，不过没有付之于实践，这次Yo2服务器崩溃，终于促使我创建自己的DDDSpace.cn

在这里要感谢[小张](http://hengtian.org/)，呵呵，让我赶上了新手空间合租，享受了性价比很高的服务，还要感谢[wordpress.org
.cn](http://wordpress.org.cn),里面很多会员的帖子给我很多帮助，让我能够快速的创建这个博客

刚弄好这个博客，还有很多工作要做，先到这里了

测试一下codercolorer

`package postbar.action;`

import java.util.ArrayList;

import org.apache.log4j.Logger;

import com.opensymphony.xwork2.ActionContext;

import postbar.bean.Category;

import postbar.bean.Topic;

import postbar.dao.CategoryDAO;

public class HomeAction {

private ArrayList categorys;

private Logger logger = Logger.getLogger(HomeAction.class);

public String execute() throws Exception {

CategoryDAO categoryDAO = new CategoryDAO();

categorys = categoryDAO.getCategorys();

// logger.info("homeAction is running");

// logger.info(ActionContext.getContext().getSession().get("userId"));

logger.info(ActionContext.getContext().getSession().get("userName"));

return "success";

}

public ArrayList getCategorys() {

return categorys;

}

public void setCategorys(ArrayList categorys) {

this.categorys = categorys;

} }

测试一下图片那个插件
[![image](/images/upload_dropbox/201612/404.png)](http://img9.2u.com.cn/desk_pic/big_247/246953.jpg)


