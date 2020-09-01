import pymongo


# 从mongodb中读取数据
# 返回数据为含有店铺名和订单数的列表
def getStores():
    list_tmp = []

    hostname = "localhost"
    port_num = int("27017")
    db_name = "stores"

    try:
        client = pymongo.MongoClient(hostname, port_num)
        # 选择数据库
        db = client[db_name]
        collection = db["Nanjing_store"]

        for r in collection.find({}, {"flavors": 1, "recent_order_num": 1}):
            for flavor in r["flavors"]:
                list_tmp.append(str(flavor["name"]) + ":" + str(r["recent_order_num"]))
        return list_tmp
    except:
        print("db connection wrong")


# 从mongodb中读取数据
# 返回数据为每个城市鸭店的数量
def getDuck():
    dbList = ["Nanjing_store", "Beijing_store", "Guangzhou_store", "Chengdu_store", "Shenyang_store"]
    CityList = ["南京", "北京", "广州", "成都", "沈阳"]
    list_tmp = []

    hostname = "localhost"
    port_num = int("27017")
    db_name = "stores"

    try:
        client = pymongo.MongoClient(hostname, port_num)
        # 选择数据库
        db = client[db_name]

        for i in range(5):
            collection = db[dbList[i]]

            for r in collection.find({}):
                if "鸭" in str(r):
                    list_tmp.append(CityList[i] + ":" + str(r["recent_order_num"]))
            return list_tmp
    except:
        print("db connection wrong")


getDuck()
