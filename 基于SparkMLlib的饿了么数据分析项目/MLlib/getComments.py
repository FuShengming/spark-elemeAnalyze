import pymongo

# 从mongodb中读取数据
# 返回数据为含有店铺名和订单数的列表

list_tmp = []

hostname = "localhost"
port_num = int("27017")
db_name = "stores"

try:
    client = pymongo.MongoClient(hostname, port_num)
    # 选择数据库
    db = client[db_name]
    collection = db["Nanjing_comments"]

    for r in collection.find({}, {"rating_text": 1}):
        print(r["rating_text"])

except:
    print("db connection wrong")