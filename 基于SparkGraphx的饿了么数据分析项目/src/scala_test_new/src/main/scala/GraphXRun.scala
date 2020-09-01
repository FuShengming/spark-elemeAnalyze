import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import org.apache.spark.{SPARK_BRANCH, SparkConf, SparkContext}
import org.apache.spark.SparkContext._
import scala.collection.mutable.ArrayBuffer
object GraphXRun {
  def main(args: Array[String]): Unit = {
    val master = "spark://172.17.231.18:7077"
    val spark_driver_host = "172.17.231.18"
    val conf:SparkConf = new SparkConf()
    conf.setAppName("Graph")
    conf.setMaster("local")

//    conf.set("spark.driver.host", spark_driver_host)
    val sc = new SparkContext(conf)

    val data=GetData.getDic("coco_comments")
    print(data)
    var vertexArray:ArrayBuffer[(Long,String)]=new ArrayBuffer()
    var edgeArray:ArrayBuffer[(Long,Long,Int)]=new ArrayBuffer()
    var index:Long=0L
    for(x<-data){
      var item1=x._1.split("_")(0)
      var item2=x._1.split("_")(1)
      var key=x._2
      var index1:Long=0
      var index2:Long=0
      var found:Boolean=false
      for(vertex:(Long,String)<-vertexArray){
        if (vertex._2.equals(item1)){
          found=true
          index1=vertex._1
        }
      }
      if(!found){
        index+=1L
        index1=index
        vertexArray.append((index1,item1))
      }
      found=false
      for(vertex:(Long,String)<-vertexArray){
        if (vertex._2.equals(item2)){
          found=true
          index2=vertex._1
        }
      }
      if(!found){
        index+=1L
        index2=index
        vertexArray.append((index2,item2))
      }
      edgeArray.append((index1,index2,key))
    }

    val vertexRDD: RDD[(Long, String)] = sc.parallelize(vertexArray)
    val edgeRDD: RDD[Edge[Int]] = sc.parallelize(edgeArray).map{x=>Edge(x._1,x._2,x._3)}
    val graph: Graph[String, Int] = Graph(vertexRDD, edgeRDD)
    graph.triplets.filter(x => x.srcId == 10L).foreach{x => printf("%s与%s在同%s个订单中", x.dstAttr,  x.srcAttr, x.attr);println()}
    graph.triplets.filter(x => x.dstId == 10L).foreach{x => printf("%s与%s在同%s个订单中", x.dstAttr,  x.srcAttr, x.attr);println()}

    println("边权重排序：")
    graph.edges.sortBy(e=>e.attr,ascending = false).top(10)(Ordering.by(_.attr)).foreach(println)
    println("点出入度排序：")
    graph.degrees.collect().sortBy(v=>v._2*(-1)).foreach(x=>println(x))
    println("PageRank排序：")
    graph.pageRank(0.001).vertices.top(10)(Ordering.by(_._2)).foreach(println)
  }
}
