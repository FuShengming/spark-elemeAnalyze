import random

import requests
import time
import saveComment
import pymongo

hostname = "localhost"
port_num = int("27017")
db_name = "stores"

# shopList=["CoCo","汉堡王","美亦粥"]
# dbList=["coco_comments", "burgerking_comments", "meiyizhou_comments"]
basicUrl="https://h5.ele.me/restapi/ugc/v3/restaurants/"
basicUrl2="/ratings?has_content=true&tag_name=%E5%B7%AE%E8%AF%84&offset="
basicUrl3="&limit=200"

header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36","host":
    "h5.ele.me"}

cookies = {
    "SID": "dVPd9rkfyk0JeW8zCaLPEkGNhePw0ry6jBlw",
    "USERID": "1329673210",
    "UTUSER": "1329673210",
    "ZDS": "1.0|1570867363|XtXDlHa9Wm1znpOUaXZzNVqjCTY4bdG78xeNVCt0iD+KPgatyp51NSVNSCystgpQ"
}



idList=[]
## 从数据库获取idList
try:
    client = pymongo.MongoClient(hostname, port_num)
    # 选择数据库
    db = client[db_name]
    collection = db["Nanjing_store"]
    for r in collection.find({}, {"id": 1}):
        idList.append(r["id"])
except:
    print("db connection wrong")

for id in idList:
    # for offset in range(0, 1600, 200):
    tempUrl=basicUrl+id+basicUrl2+"0"+basicUrl3
    try:
        data = requests.get(tempUrl, headers=header, cookies=cookies)
    except Exception as e:
        print(e.args)
        time.sleep(60)
        data = requests.get(tempUrl, headers=header, cookies=cookies)
    data.encoding = 'utf-8'
    content = data.text
    ##Todo: content存入数据库,注意不同店铺存入不同列表
    try:
        client = pymongo.MongoClient(hostname, port_num)
        # 选择数据库
        db = client[db_name]
        # 保存爬取的数据到MongoDB
        ls = saveComment.pre_process(content)
        saveComment.save_comment(ls, db, "Nanjing_comments")
    except Exception as e:
        print("db connection wrong")

    time.sleep(random.randint(10, 40))


