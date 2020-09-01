import random

import requests
import time
import pymongo

import functions
import saveToDatabase

hostname = "localhost"
port_num = int("27017")
db_name = "stores"

cityList = ["南京", "北京", "广州", "成都", "沈阳"]
latiAndlongiList = [[[31.969385, 118.699734], [32.117435, 118.951682]]]

##每个城市挑选两组经纬度，遍历以这两个点为相对顶点（左下顶点与右上顶点）的矩形区域中所有店铺信息


dbList = ["Nanjing_store"]

basicUrl = "https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=&longitude=&keyword=&offset="  ##饿了么店铺信息url基本格式

basicLimit = "&limit=200"  ##limit参数：店铺信息Json中每一页显示的店铺条数

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "host": "h5.ele.me"}
cookies = {
    "SID": "dVPd9rkfyk0JeW8zCaLPEkGNhePw0ry6jBlw",
    "USERID": "1329673210",
    "UTUSER": "1329673210",
    "ZDS": "1.0|1570867363|XtXDlHa9Wm1znpOUaXZzNVqjCTY4bdG78xeNVCt0iD+KPgatyp51NSVNSCystgpQ"
}
shopIdList = []  ##店铺id列表

failStr = "{\"message\":\"用户网络信息异常\",\"name\":\"NEED_SLIDE\"}"  ##账号被ban后获取的json

voidStr = "{\"has_next\":false,\"items\":[],\"meta\":{\"rank_id\":\"\"}}"  ##当前位置所有店铺信息获取完毕后获取到的空json

for i in range(0, 1):

    latitudeMin = latiAndlongiList[i][0][0]
    latitudeMax = latiAndlongiList[i][1][0]
    longitudeMin = latiAndlongiList[i][0][1]
    longitudeMax = latiAndlongiList[i][1][1]

    latiStep = (latitudeMax - latitudeMin) / 10
    longiStep = (longitudeMax - longitudeMin) / 10
    ## 每个城市遍历5x5=25个经纬度

    while (latitudeMin < latitudeMax):
        while (longitudeMin < longitudeMax):

            url = functions.urlExtend(basicUrl, [latitudeMin, longitudeMin])
            print("Current position is " + str(latitudeMin) + " " + str(longitudeMin))

            for j in range(0, 500, 30):
                print("Searching page " + str(j // 30 + 1))
                tempurl = url + str(j) + basicLimit
                try:
                    data = requests.get(tempurl, headers=header, cookies=cookies)
                except:
                    time.sleep(60)
                    data = requests.get(tempurl, headers=header, cookies=cookies)
                data.encoding = 'utf-8'
                content = data.text
                print(content)
                if content == failStr:
                    print("spider fail")  ##账号被ban输出异常提示
                    break
                if content == voidStr:  ##当前经纬度位置遍历完毕
                    break

                notRepeatJson = functions.getNotRepeatJson(functions.stringToJson(content),
                                                           shopIdList)  ##通过店铺id列表对当前Json进行去重

                functions.addResIdToList(content, shopIdList)  ##储存店铺id列表

                try:
                    client = pymongo.MongoClient(hostname, port_num)
                    # 选择数据库
                    db = client[db_name]
                    # 保存爬取的数据到MongoDB
                    saveToDatabase.save_store(notRepeatJson, db, dbList[i])
                except:
                    print("db connection wrong")

                # print(shopIdList)
                # print(notRepeatJson)
                time.sleep(random.randint(15, 30))

            longitudeMin += longiStep
            longitudeMin = round(longitudeMin, 6)  ##防止出现浮点数误差
        latitudeMin += latiStep
        latitudeMin = round(latitudeMin, 6)  ##防止出现浮点数误差
