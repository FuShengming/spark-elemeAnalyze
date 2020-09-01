import json
import re


# 将各地店铺信息存入数据库
def save_store(ls, db, db_name):
    # 选择数据的collection
    collection = db[db_name]
    count = 0

    for t in ls:
        s = t.get('restaurant')
        # 要存储的信息
        temp = {"flavors": s["flavors"], "id": s["id"], "folding_restaurants": 0,
                "latitude": s["latitude"], "longitude": s["longitude"], "name": s["name"],
                "opening_hours": s["opening_hours"], "rating": s["rating"],
                "rating_count": s["rating_count"], "recent_order_num": s["recent_order_num"],
                "recommend_reasons": s["recommend_reasons"]
                }
        if "folding_restaurants" in s:
            temp["folding_restaurants"] = len(s["folding_restaurants"])
        count += 1
        # 存入数据库
        collection.insert_one(temp)

    print(str(count) + " saved")


def save_comment(ls, db, db_name):
    # 选择数据的collection
    collection = db["comments"]
    count = 0
    try:
        for s in ls:
            temp = {"food_ratings": s["food_ratings"], "rated_at": s["rated_at"], "rating": s["rating"],
                    "rating_text": s["rating_text"], "is_delay": "false"
                    }
            if s["time_spent_desc"] != "":
                temp["is_delay"] = "true"
            print(temp)
            count += 1
            collection.insert_one(temp)
    except Exception as e:
        print(e.args)
        print("read to json wrong", count)
    print(count)
