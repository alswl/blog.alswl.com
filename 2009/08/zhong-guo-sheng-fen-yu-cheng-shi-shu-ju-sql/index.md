

本文来源：[中国省份与城市数据插入 - xlx - CSDN博客](http://blog.csdn.net/xielingxu/archive/2007/08/26/1759471.aspx)

在Google找到这个，实在是爱不释手，就转过来了，很多项目都需要用到这些数据。


```
if exists (select * from sysobjects where id = OBJECT_ID('[province]') and OBJECTPROPERTY(id, 'IsUserTable') = 1)
DROP TABLE [province]

CREATE TABLE [province] (

[id] [int] NOT NULL,

[provinceID] [nvarchar] (12) NOT NULL,

[province] [nvarchar] (80) NOT NULL)

ALTER TABLE [province] WITH NOCHECK ADD CONSTRAINT [PK_province] PRIMARY KEY
NONCLUSTERED ( [id] )INSERT [province] ([id],[provinceID],[province]) VALUES (
1,'110000','北京市')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 2,'120000','天津市')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 3,'130000','河北省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 4,'140000','山西省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 5,'150000','内蒙古自治区')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 6,'210000','辽宁省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 7,'220000','吉林省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 8,'230000','黑龙江省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 9,'310000','上海市')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 10,'320000','江苏省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 11,'330000','浙江省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 12,'340000','安徽省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 13,'350000','福建省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 14,'360000','江西省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 15,'370000','山东省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 16,'410000','河南省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 17,'420000','湖北省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 18,'430000','湖南省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 19,'440000','广东省')

INSERT [province] ([id],[provinceID],[province]) VALUES (
20,'450000','广西壮族自治区')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 21,'460000','海南省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 22,'500000','重庆市')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 23,'510000','四川省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 24,'520000','贵州省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 25,'530000','云南省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 26,'540000','西藏自治区')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 27,'610000','陕西省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 28,'620000','甘肃省')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 29,'630000','青海省')

INSERT [province] ([id],[provinceID],[province]) VALUES (
30,'640000','宁夏回族自治区')

INSERT [province] ([id],[provinceID],[province]) VALUES (
31,'650000','新疆维吾尔自治区')

INSERT [province] ([id],[provinceID],[province]) VALUES ( 32,'710000','台湾省')

INSERT [province] ([id],[provinceID],[province]) VALUES (
33,'810000','香港特别行政区')

INSERT [province] ([id],[provinceID],[province]) VALUES (
34,'820000','澳门特别行政区')

if exists (select * from sysobjects where id = OBJECT_ID('[area]') and
OBJECTPROPERTY(id, 'IsUserTable') = 1)

DROP TABLE [area]

CREATE TABLE [area] (

[id] [int] NOT NULL,

[cityID] [nvarchar] (12) NOT NULL,

[city] [nvarchar] (100) NOT NULL,

[father] [nvarchar] (12) NOT NULL)

ALTER TABLE [area] WITH NOCHECK ADD CONSTRAINT [PK_area] PRIMARY KEY
NONCLUSTERED ( [id] )INSERT [area] ([id],[cityID],[city],[father]) VALUES (
1,'110100','市辖区','110000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
2,'110200','县','110000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
3,'120100','市辖区','120000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
4,'120200','县','120000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
5,'130100','石家庄市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
6,'130200','唐山市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
7,'130300','秦皇岛市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
8,'130400','邯郸市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
9,'130500','邢台市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
10,'130600','保定市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
11,'130700','张家口市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
12,'130800','承德市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
13,'130900','沧州市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
14,'131000','廊坊市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
15,'131100','衡水市','130000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
16,'140100','太原市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
17,'140200','大同市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
18,'140300','阳泉市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
19,'140400','长治市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
20,'140500','晋城市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
21,'140600','朔州市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
22,'140700','晋中市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
23,'140800','运城市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
24,'140900','忻州市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
25,'141000','临汾市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
26,'141100','吕梁市','140000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
27,'150100','呼和浩特市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
28,'150200','包头市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
29,'150300','乌海市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
30,'150400','赤峰市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
31,'150500','通辽市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
32,'150600','鄂尔多斯市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
33,'150700','呼伦贝尔市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
34,'150800','巴彦淖尔市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
35,'150900','乌兰察布市','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
36,'152200','兴安盟','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
37,'152500','锡林郭勒盟','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
38,'152900','阿拉善盟','150000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
39,'210100','沈阳市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
40,'210200','大连市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
41,'210300','鞍山市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
42,'210400','抚顺市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
43,'210500','本溪市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
44,'210600','丹东市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
45,'210700','锦州市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
46,'210800','营口市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
47,'210900','阜新市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
48,'211000','辽阳市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
49,'211100','盘锦市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
50,'211200','铁岭市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
51,'211300','朝阳市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
52,'211400','葫芦岛市','210000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
53,'220100','长春市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
54,'220200','吉林市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
55,'220300','四平市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
56,'220400','辽源市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
57,'220500','通化市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
58,'220600','白山市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
59,'220700','松原市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
60,'220800','白城市','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
61,'222400','延边朝鲜族自治州','220000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
62,'230100','哈尔滨市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
63,'230200','齐齐哈尔市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
64,'230300','鸡西市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
65,'230400','鹤岗市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
66,'230500','双鸭山市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
67,'230600','大庆市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
68,'230700','伊春市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
69,'230800','佳木斯市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
70,'230900','七台河市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
71,'231000','牡丹江市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
72,'231100','黑河市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
73,'231200','绥化市','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
74,'232700','大兴安岭地区','230000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
75,'310100','市辖区','310000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
76,'310200','县','310000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
77,'320100','南京市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
78,'320200','无锡市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
79,'320300','徐州市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
80,'320400','常州市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
81,'320500','苏州市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
82,'320600','南通市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
83,'320700','连云港市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
84,'320800','淮安市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
85,'320900','盐城市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
86,'321000','扬州市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
87,'321100','镇江市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
88,'321200','泰州市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
89,'321300','宿迁市','320000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
90,'330100','杭州市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
91,'330200','宁波市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
92,'330300','温州市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
93,'330400','嘉兴市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
94,'330500','湖州市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
95,'330600','绍兴市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
96,'330700','金华市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
97,'330800','衢州市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
98,'330900','舟山市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
99,'331000','台州市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
100,'331100','丽水市','330000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
101,'340100','合肥市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
102,'340200','芜湖市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
103,'340300','蚌埠市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
104,'340400','淮南市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
105,'340500','马鞍山市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
106,'340600','淮北市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
107,'340700','铜陵市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
108,'340800','安庆市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
109,'341000','黄山市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
110,'341100','滁州市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
111,'341200','阜阳市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
112,'341300','宿州市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
113,'341400','巢湖市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
114,'341500','六安市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
115,'341600','亳州市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
116,'341700','池州市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
117,'341800','宣城市','340000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
118,'350100','福州市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
119,'350200','厦门市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
120,'350300','莆田市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
121,'350400','三明市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
122,'350500','泉州市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
123,'350600','漳州市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
124,'350700','南平市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
125,'350800','龙岩市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
126,'350900','宁德市','350000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
127,'360100','南昌市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
128,'360200','景德镇市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
129,'360300','萍乡市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
130,'360400','九江市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
131,'360500','新余市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
132,'360600','鹰潭市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
133,'360700','赣州市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
134,'360800','吉安市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
135,'360900','宜春市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
136,'361000','抚州市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
137,'361100','上饶市','360000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
138,'370100','济南市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
139,'370200','青岛市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
140,'370300','淄博市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
141,'370400','枣庄市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
142,'370500','东营市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
143,'370600','烟台市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
144,'370700','潍坊市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
145,'370800','济宁市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
146,'370900','泰安市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
147,'371000','威海市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
148,'371100','日照市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
149,'371200','莱芜市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
150,'371300','临沂市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
151,'371400','德州市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
152,'371500','聊城市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
153,'371600','滨州市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
154,'371700','荷泽市','370000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
155,'410100','郑州市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
156,'410200','开封市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
157,'410300','洛阳市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
158,'410400','平顶山市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
159,'410500','安阳市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
160,'410600','鹤壁市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
161,'410700','新乡市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
162,'410800','焦作市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
163,'410900','濮阳市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
164,'411000','许昌市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
165,'411100','漯河市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
166,'411200','三门峡市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
167,'411300','南阳市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
168,'411400','商丘市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
169,'411500','信阳市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
170,'411600','周口市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
171,'411700','驻马店市','410000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
172,'420100','武汉市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
173,'420200','黄石市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
174,'420300','十堰市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
175,'420500','宜昌市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
176,'420600','襄樊市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
177,'420700','鄂州市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
178,'420800','荆门市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
179,'420900','孝感市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
180,'421000','荆州市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
181,'421100','黄冈市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
182,'421200','咸宁市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
183,'421300','随州市','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
184,'422800','恩施土家族苗族自治州','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
185,'429000','省直辖行政单位','420000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
186,'430100','长沙市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
187,'430200','株洲市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
188,'430300','湘潭市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
189,'430400','衡阳市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
190,'430500','邵阳市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
191,'430600','岳阳市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
192,'430700','常德市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
193,'430800','张家界市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
194,'430900','益阳市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
195,'431000','郴州市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
196,'431100','永州市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
197,'431200','怀化市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
198,'431300','娄底市','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
199,'433100','湘西土家族苗族自治州','430000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
200,'440100','广州市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
201,'440200','韶关市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
202,'440300','深圳市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
203,'440400','珠海市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
204,'440500','汕头市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
205,'440600','佛山市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
206,'440700','江门市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
207,'440800','湛江市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
208,'440900','茂名市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
209,'441200','肇庆市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
210,'441300','惠州市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
211,'441400','梅州市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
212,'441500','汕尾市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
213,'441600','河源市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
214,'441700','阳江市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
215,'441800','清远市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
216,'441900','东莞市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
217,'442000','中山市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
218,'445100','潮州市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
219,'445200','揭阳市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
220,'445300','云浮市','440000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
221,'450100','南宁市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
222,'450200','柳州市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
223,'450300','桂林市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
224,'450400','梧州市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
225,'450500','北海市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
226,'450600','防城港市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
227,'450700','钦州市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
228,'450800','贵港市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
229,'450900','玉林市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
230,'451000','百色市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
231,'451100','贺州市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
232,'451200','河池市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
233,'451300','来宾市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
234,'451400','崇左市','450000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
235,'460100','海口市','460000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
236,'460200','三亚市','460000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
237,'469000','省直辖县级行政单位','460000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
238,'500100','市辖区','500000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
239,'500200','县','500000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
240,'500300','市','500000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
241,'510100','成都市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
242,'510300','自贡市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
243,'510400','攀枝花市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
244,'510500','泸州市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
245,'510600','德阳市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
246,'510700','绵阳市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
247,'510800','广元市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
248,'510900','遂宁市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
249,'511000','内江市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
250,'511100','乐山市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
251,'511300','南充市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
252,'511400','眉山市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
253,'511500','宜宾市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
254,'511600','广安市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
255,'511700','达州市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
256,'511800','雅安市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
257,'511900','巴中市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
258,'512000','资阳市','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
259,'513200','阿坝藏族羌族自治州','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
260,'513300','甘孜藏族自治州','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
261,'513400','凉山彝族自治州','510000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
262,'520100','贵阳市','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
263,'520200','六盘水市','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
264,'520300','遵义市','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
265,'520400','安顺市','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
266,'522200','铜仁地区','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
267,'522300','黔西南布依族苗族自治州','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
268,'522400','毕节地区','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
269,'522600','黔东南苗族侗族自治州','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
270,'522700','黔南布依族苗族自治州','520000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
271,'530100','昆明市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
272,'530300','曲靖市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
273,'530400','玉溪市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
274,'530500','保山市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
275,'530600','昭通市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
276,'530700','丽江市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
277,'530800','思茅市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
278,'530900','临沧市','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
279,'532300','楚雄彝族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
280,'532500','红河哈尼族彝族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
281,'532600','文山壮族苗族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
282,'532800','西双版纳傣族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
283,'532900','大理白族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
284,'533100','德宏傣族景颇族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
285,'533300','怒江傈僳族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
286,'533400','迪庆藏族自治州','530000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
287,'540100','拉萨市','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
288,'542100','昌都地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
289,'542200','山南地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
290,'542300','日喀则地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
291,'542400','那曲地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
292,'542500','阿里地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
293,'542600','林芝地区','540000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
294,'610100','西安市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
295,'610200','铜川市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
296,'610300','宝鸡市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
297,'610400','咸阳市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
298,'610500','渭南市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
299,'610600','延安市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
300,'610700','汉中市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
301,'610800','榆林市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
302,'610900','安康市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
303,'611000','商洛市','610000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
304,'620100','兰州市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
305,'620200','嘉峪关市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
306,'620300','金昌市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
307,'620400','白银市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
308,'620500','天水市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
309,'620600','武威市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
310,'620700','张掖市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
311,'620800','平凉市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
312,'620900','酒泉市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
313,'621000','庆阳市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
314,'621100','定西市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
315,'621200','陇南市','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
316,'622900','临夏回族自治州','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
317,'623000','甘南藏族自治州','620000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
318,'630100','西宁市','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
319,'632100','海东地区','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
320,'632200','海北藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
321,'632300','黄南藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
322,'632500','海南藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
323,'632600','果洛藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
324,'632700','玉树藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
325,'632800','海西蒙古族藏族自治州','630000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
326,'640100','银川市','640000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
327,'640200','石嘴山市','640000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
328,'640300','吴忠市','640000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
329,'640400','固原市','640000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
330,'640500','中卫市','640000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
331,'650100','乌鲁木齐市','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
332,'650200','克拉玛依市','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
333,'652100','吐鲁番地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
334,'652200','哈密地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
335,'652300','昌吉回族自治州','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
336,'652700','博尔塔拉蒙古自治州','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
337,'652800','巴音郭楞蒙古自治州','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
338,'652900','阿克苏地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
339,'653000','克孜勒苏柯尔克孜自治州','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
340,'653100','喀什地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
341,'653200','和田地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
342,'654000','伊犁哈萨克自治州','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
343,'654200','塔城地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
344,'654300','阿勒泰地区','650000')

INSERT [area] ([id],[cityID],[city],[father]) VALUES (
345,'659000','省直辖行政单位','650000')

```
