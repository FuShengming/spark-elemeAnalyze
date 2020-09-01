基于Spark Graphx的饿了么数据分析

组长：
171250640 付圣铭
组员：
171250532 苗朗宁
171250559 王煜霄


文件说明：
/src/main/scala

GetData.scala : 评论数据的读取预处理方法，被GraphXRun依赖
GraphXRun.scala： Graphx的启动以及主程序

/src/main/python

rateSpider.py：评论爬取与存储
saveComment.py ：评论存储的依赖方法
