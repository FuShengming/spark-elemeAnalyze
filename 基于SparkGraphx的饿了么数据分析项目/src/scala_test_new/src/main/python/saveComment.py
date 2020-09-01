import json


def pre_process(dicts):
    left = 0
    right = 0
    start = 0
    ls = []
    for i in range(1, len(dicts)):
        if dicts[i] == "{":
            left += 1
            if left == 1:
                start = i
        elif dicts[i] == "}":
            right += 1
        elif dicts[i] == "," and right == left:
            continue
        elif dicts[i] == "]" and right == left:
            continue
        elif left == right:
            continue

        if right == left:
            dict1 = dicts[start:(i + 1)]
            data1 = json.loads(dict1)
            ls.append(data1)
            left = 0
            right = 0
    return ls


def save_comment(ls, db, db_name):
    # 选择数据的collection
    collection = db[db_name]
    count = 0
    try:
        for s in ls:
            sp = ""
            items = ""
            items_rating = ""
            items_rating_text = ""
            for item in s["food_ratings"]:
                items += sp + item["rate_name"]
                items_rating += sp + str(item["rating"])
                items_rating_text += sp + item["rating_text"]
                sp = "; "
            temp = {"items": items, "items_rating": items_rating, "items_rating_text": items_rating_text,
                    "rated_at": s["rated_at"], "rating": s["rating"], "rating_text": s["rating_text"]}
            # print(temp)
            count += 1
            collection.insert_one(temp)
    except Exception as e:
        print(e.args)
        print("read to json wrong", count)
    print(str(count) + " saved.")
