from pyspark.ml.classification import NaiveBayes,LogisticRegression
from pyspark.ml.feature import RegexTokenizer,CountVectorizer,StringIndexer,HashingTF,IDF
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.sql import SQLContext
from pyspark import SparkConf,SparkContext

appname = "count"  # 任务名称
master = "spark://172.17.231.18:7077"  # "spark://host:port"
spark_driver_host = "172.17.231.18"  # 本地主机ip
conf = SparkConf()\
    .setAppName(appname)\
    .setMaster(master)\
    .set("spark.driver.host", spark_driver_host)\
    .set("spark.streaming.blockInterval", "50ms")\
    .set("spark.driver.memory", "4g")

sc=SparkContext(conf=conf)
##sc=SparkContext()
sqlContext=SQLContext(sc)
data=sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load('C:/Users/Admin/Desktop/Mllib/Training.txt')
data.show(5)

data.groupBy("Category").count().orderBy("count",ascending=False).show()

# regexTokenizer=RegexTokenizer(inputCol="Comment",outputCol="words")
# countVectors=CountVectorizer(inputCol="words",outputCol="features")
# labelStringIndex=StringIndexer(inputCol="Category",outputCol="label")
# pipeline=Pipeline(stages=[regexTokenizer,countVectors,labelStringIndex])

regexTokenizer=RegexTokenizer(inputCol="Comment",outputCol="words")
labelStringIndex=StringIndexer(inputCol="Category",outputCol="label")
hashingTF=HashingTF(inputCol="words",outputCol="rawFeatures",numFeatures=600)
idf=IDF(inputCol="rawFeatures",outputCol="features",minDocFreq=3) # minDocFreq=5
pipeline=Pipeline(stages=[regexTokenizer,hashingTF,idf,labelStringIndex])

pipelineFit=pipeline.fit(data)
dataset=pipelineFit.transform(data)
dataset.show(5)

(trainingData, testData) = dataset.randomSplit([0.75, 0.25], seed = 0)
nb=NaiveBayes(smoothing=1)
model=nb.fit(trainingData)
predictions=model.transform(testData)
predictions.select("label","prediction").\
    filter(predictions['prediction']!=predictions['label']).\
    groupBy('label','prediction').count().\
    show()
predictions.select("label","prediction","probability","Comment").\
    filter(predictions['prediction']!=predictions['label']).\
    show(truncate=100)

# lr = LogisticRegression(maxIter=20, regParam=0.3, elasticNetParam=0)
# lrModel = lr.fit(trainingData)
# predictions = lrModel.transform(testData)
# predictions.select("label","probability","prediction").show(truncate=100)

print("测试集准确度:")
evaluator=MulticlassClassificationEvaluator(predictionCol="prediction")
print(evaluator.evaluate(predictions))

p_data=sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load('C:/Users/Admin/Desktop/Mllib/All.txt')
p_pipeline=Pipeline(stages=[regexTokenizer,hashingTF,idf])
p_pipelineFit=p_pipeline.fit(p_data)
p_dataset=p_pipelineFit.transform(p_data)
p_dataset.show(5)
p_predictions=model.transform(p_dataset)
p_predictions.select("Comment","probability","prediction").show(truncate=100)
p_predictions.groupBy("prediction").count().show()