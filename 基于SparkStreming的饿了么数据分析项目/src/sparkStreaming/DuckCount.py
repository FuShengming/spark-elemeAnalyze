from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
import sys
import getData
appname = "count"  # 任务名称
master = "spark://172.17.231.18:7077"  # "spark://host:port"
spark_driver_host = "172.17.231.18"  # 本地主机ip
conf = SparkConf()\
    .setAppName(appname)\
    .setMaster(master)\
    .set("spark.driver.host", spark_driver_host)\
    .set("spark.streaming.blockInterval", "50ms")\
    .set("spark.driver.memory", "4g")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 1)

#queueStream
lineQueue = []
lineList=getData.getDuck()
lineQueue+=[sc.parallelize(lineList)]
lineStream = ssc.queueStream(lineQueue)
lineStream.pprint()
wordStream=lineStream.map(lambda x : (x.split(":")[0],int(x.split(":")[1])))
reducedStream = wordStream.reduceByKey(lambda a, b: a + b)
reducedStream.saveAsTextFiles('D:/data/duck/Duck_order')
reducedStream.pprint()

ssc.start()
ssc.awaitTermination()
