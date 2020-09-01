import os

cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
# city="Beijing"
for city in cities:
    print(city)
    docList = os.listdir('D:/data/recent_order_num/'+city+'/')  # 特定目录下的文件存入列表
    docList.sort()  # 显示当前文件夹下所有文件并进行排序

    for i in docList:
        print(i)  # 输出文件名

    fname = open('D:/data/recent_order_num/merge_'+city+'.txt', "wb")  # 创建文件
    for i in docList:
        x = open('D:/data/recent_order_num/'+city+'/'+i, "rb")  # 打开列表中的文件,读取文件内容
        fname.write(x.read())  # 写入新建的log文件中
        x.close()  # 关闭列表文件

    fname.close()

    docList = os.listdir('D:/data/shop_num/' + city + '/')  # 特定目录下的文件存入列表
    docList.sort()  # 显示当前文件夹下所有文件并进行排序

    for i in docList:
        print(i)  # 输出文件名

    fname = open('D:/data/shop_num/merge_'+city+'.txt', "wb")  # 创建文件

    for i in docList:
        x = open('D:/data/shop_num/' + city + '/' + i, "rb")  # 打开列表中的文件,读取文件内容
        fname.write(x.read())  # 写入新建的log文件中
        x.close()  # 关闭列表文件

    fname.close()