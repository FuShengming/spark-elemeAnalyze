import random

import requests
import time
import saveComment
import pymongo

hostname = "localhost"
port_num = int("27017")
db_name = "stores"

shopList=["CoCo","汉堡王","美亦粥"]
dbList=["coco_comments", "burgerking_comments", "meiyizhou_comments"]
basicUrl="https://h5.ele.me/restapi/ugc/v3/restaurants/"
basicUrl2="/ratings?tag_name=%E5%85%A8%E9%83%A8&offset=0&limit=200"

header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36","host":
    "h5.ele.me"}

cookies = {
    "SID": "dVPd9rkfyk0JeW8zCaLPEkGNhePw0ry6jBlw",
    "USERID": "1329673210",
    "UTUSER": "1329673210",
    "ZDS": "1.0|1570867363|XtXDlHa9Wm1znpOUaXZzNVqjCTY4bdG78xeNVCt0iD+KPgatyp51NSVNSCystgpQ"
}

for i in range(0,3):

    idList=["E13914966037341923803", "E10607269214564345126"]
    '''##Todo  从数据库获取idList
    try:
        client = pymongo.MongoClient(hostname, port_num)
        # 选择数据库
        db = client[db_name]
        collection = db["Nanjing_store"]
        shop_name = "^("+shopList[i]+")"
        for r in collection.find({"name": {"$regex": shop_name}}, {"id": 1}):
            idList.append(r["id"])
    except:
        print("db connection wrong")'''

    for id in idList:
        tempUrl=basicUrl+id+basicUrl2
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
            saveComment.save_comment(ls, db, dbList[i])
        except Exception as e:
            print("db connection wrong")

        time.sleep(random.randint(15, 30))


