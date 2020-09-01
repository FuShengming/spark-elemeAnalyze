from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
from operator import add
import time
import getData

# city="Beijing"
# city="Chengdu"
# city="Guangzhou"
# city="Nanjing"
city = "Shenyang"
appname = "count"  # 任务名称
master = "spark://192.168.76.1:7077"  # "spark://host:port"
spark_driver_host = "192.168.76.1"  # 本地主机ip
conf = SparkConf() \
    .setAppName(appname) \
    .setMaster(master) \
    .set("spark.driver.host", spark_driver_host) \
    .set("spark.streaming.blockInterval", "50ms") \
    .set("spark.driver.memory", "4g")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 1)

# queueStream
lineQueue = []
# rdd = sc.textFile('D:/data/'+city+'.txt')
# def getSet(line):
#     return (line.split(":")[1],line.split(":")[0])
# rdd=rdd.map(getSet)
lineList = getData.getStores()

# for line in lineList:
#     lineQueue += [sc.parallelize([line])]#给line套上[]是为了一个句子作为一整个元素（一整个数组中只有该行一个元素），否则会被序列化切得稀碎

# batch_number=10
# for i in range(0,len(lineList),batch_number):
#     line=""
#     for j in range(batch_number):
#         if(i+j<len(lineList)):
#             line+=lineList[i+j]
#     lineQueue += [sc.parallelize([line])]

# for i in lineList:
#     lineQueue+=[sc.parallelize([i])]
# batch_size=1000
# for i in range(0,len(lineList),batch_size):
#     batch=[]
#     for j in range(batch_size):
#         if (i+j)<len(lineList):
#             batch.append(lineList[i+j])
#     lineQueue+=[sc.parallelize(batch)]
lineQueue += [sc.parallelize(lineList)]
lineStream = ssc.queueStream(lineQueue)
lineStream.pprint()
wordStream = lineStream.map(lambda x: (x.split(":")[0], int(x.split(":")[1])))
reducedStream = wordStream.reduceByKey(lambda a, b: a + b)
reducedStream.saveAsTextFiles('D:/data/recent_order_num/' + city)
reducedStream.pprint()

ssc.start()
ssc.awaitTermination()
