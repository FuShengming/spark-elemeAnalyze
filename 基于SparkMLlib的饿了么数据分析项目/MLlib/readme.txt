基于Spark MLlib的饿了么评论分类

组长：171250640 付圣铭
组员：171250532 苗朗宁 171250559 王煜霄

文件说明：

Bar.py : 生成柱形图
NaiveBayes.py ：spark MLlib主文件
seg.py : 分词
YellowBrick.py：将tf-idf特征向量通过t-SNE算法降维进行可视化
getComments.py : 从数据库中获取数据
rateSpider.py： 评论爬虫
restaurantSpider.py： 商铺爬虫
saveComment.py： 将评论存入数据库
saveToDatabase.py： 将店铺信息存入数据库
