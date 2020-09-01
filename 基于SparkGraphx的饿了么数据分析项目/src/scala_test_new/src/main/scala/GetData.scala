import com.mongodb.BasicDBObject
import com.mongodb.casbah.commons.MongoDBObject
import org.json4s._

import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.io.Source
import com.mongodb.casbah.{MongoClient, MongoDB}
/**
 * @Description spark graphx demo
 * @Author lay
 * @Date 2018/12/09 20:19
 */
object GetData {
  def createDatabase(url: String, port: Int, dbName: String): MongoDB = {
    MongoClient(url, port).getDB(dbName)
  }

  def getComments(dbName: String): String ={
    //连接到MongoDB
    var collection= createDatabase("localhost", 27017, "stores").getCollection(dbName)
    //println("=========从MongoDB查询数据===================")
    val res= collection.find()
    var result = ""
    while (res.hasNext()){
      val temp= res.next().get("items").asInstanceOf[String]
      //println(temp)
      result = result + "{\n"
      val items = temp.split("; ")
      items.foreach(x => result = result + x + "\n")
      result = result + "}\n"
    }
    return result
  }

  def getDic(dbName: String): mutable.Map[String, Int] ={
    var userData: ArrayBuffer[String] = ArrayBuffer()
    //从MongoDB中爬取数据
    val source1 = getComments(dbName)
    var thisOrder:ArrayBuffer[String]=ArrayBuffer()
    var relationData:mutable.Map[String,Int]=mutable.Map()
    val lines = source1.split("\n")
    var boo=false
    for ( x <- lines){

      if(x=="}"){
        boo=false
        //将此订单信息加入关系map中
        relationToMap(thisOrder,relationData)
        thisOrder.clear()

      }
      if(boo){
        var a=x
        //去除诸如大杯小杯等标签
        if (x.contains("/")){
           a=x.substring(0,x.indexOf("/"))
        }
        if (a.contains("-")){
          a=a.substring(0,a.indexOf("/"))
        }
        if (a.contains("(")){
          a=a.substring(0,a.indexOf("/"))
        }
        if (a.contains("（")){
          a=a.substring(0,a.indexOf("/"))
        }
        if(!userData.contains(a)) {
          userData.append(a)
        }

        thisOrder.append(a)
      }
      if(x=="{"){

        boo=true

      }
    }

    return relationData
  }


  def  relationToMap(array:ArrayBuffer[String],map:mutable.Map[String,Int]): Unit ={
    var a=0
    var b=0

    for(a <- 1 to array.length){

      for(b <- a+1 to array.length){

        var relationString:String=""
        var diverseString:String=""



        relationString=array(a-1)+"_"+array(b-1)
        diverseString=array(b-1)+"_"+array(a-1)
        //出现在同一订单中的商品用下划线连接
        if(map.contains(relationString)){

          map(relationString)+=1
        }
        else if(map.contains(diverseString)){

          map(diverseString)+=1
        }
        else{
          map+=(relationString->1)
        }
      }
    }
  }
}