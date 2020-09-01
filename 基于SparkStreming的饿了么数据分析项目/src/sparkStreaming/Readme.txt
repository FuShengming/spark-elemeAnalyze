SparkStreaming作业
主题：基于spark streaming的饿了么数据分析
组长：171250640 付圣铭
组员：171250559 王煜霄 171250532 苗朗宁


文件说明：

/.
restaurantSipder.py -店铺爬虫
functions.py -店铺爬虫依赖的方法

getData.py - 从MongoDB数据库中读取所需要的数据
saveToDatabase.py - 连接到MongoDB数据库，将爬取到的数据存入数据库

DuckCount.py - 使用Spark Streaming统计鸭子店铺数量 
RecentOrderNumCount.py - 使用Spark Streaming统计订单数量 
ShopNumCount.py - 使用SparkStreaming统计店铺数量 
PartMerge.py - 合并Spark Streaming生成文件
RatioCalculate.py - 计算比例
AverageCalculate.py - 计算销量算数平均
WeightedRankCalculate.py - 计算销量加权平均

/creatGraph
Bar.py - 生成柱状图
Pie.py - 生成饼状图
WordCloud_num.py - 生成店铺数量词云图
WordCloud_order_num.py - 生成订单数量词云图
WordCloud_WR.py - 生成销量加权平均词云图


