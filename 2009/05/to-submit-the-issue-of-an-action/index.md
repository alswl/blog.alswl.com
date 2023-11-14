

贴吧在提交帖子时候必须提供贴吧分类id categoryId，但是怎么把这个id提交到PostAction就比较麻烦了，在jsp页面中我试了好多办法，尝试使
用param和hidden（baidu用的hidden）标签，但是都不能读出cagegory.jsp页面的categoryId值。

最后我索性用试所有的表达式

    
    
    <s:hidden name="topicCategoryId" value="%{#categoryId}" />
    <s:hidden name="topicCategoryId" value="#categoryId" />
    <s:hidden name="topicCategoryId" value="%{categoryId}" />

最后一个果然有效。。。

貌似记得这是OPGL表达式？****


