import json

## 将经纬度加入基础url
def urlExtend(basicUrl, li):
    index1 = basicUrl.find("=")
    resUrl = basicUrl[0:index1 + 1] + str(li[0]) + basicUrl[index1 + 1:len(basicUrl)]
    index2 = resUrl.find("=", index1 + 1, len(resUrl))
    print(resUrl)
    print(index2)
    resUrl = resUrl[0:index2 + 1] + str(li[1]) + resUrl[index2 + 1:len(resUrl)]
    return resUrl


def stringToJson(string):
    return json.loads(string)


def jsonToString(myjson):
    return json.dumps(myjson)

##将店铺id加入店铺id列表
def addResIdToList(string, idList):
    myJson = stringToJson(string)
    for restaurants in myJson["items"]:
        restaurant = restaurants["restaurant"]
        idstring = restaurant["scheme"]
        id = idstring[idstring.find("=") + 1:]
        if id[0] != "E":
            continue
        if id not in idList:
            idList.append(id)


def idInList(string, idList):
    myJson = stringToJson(string)
    idstring = myJson["items"][0]["restaurant"]["scheme"]
    id = idstring[idstring.find("=") + 1:]
    if not id in idList:
        return True
    else:
        return False

## Json店铺去重
def getNotRepeatJson(myJson, shopIdList):
    for restaurants in myJson["items"]:
        restaurant = restaurants["restaurant"]
        idstring = restaurant["scheme"]
        id = idstring[idstring.find("=") + 1:]
        if id[0] != "E":
            continue
        if id in shopIdList:
            myJson["items"].remove(restaurants)

    return myJson["items"]
