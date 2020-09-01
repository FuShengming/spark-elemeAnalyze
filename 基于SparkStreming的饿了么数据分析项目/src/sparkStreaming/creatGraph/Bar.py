import matplotlib.pyplot as plt

cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
for city in cities:
    text = {}
    fname = open('D:/data/weighted_rank/10/rank_' + city + '.txt', "r")
    while True:
        s = fname.readline()
        if s == "":
            break
        s = str(s)
        if s.split(",")[0][2:-1]!='其他快餐':
            text.update({s.split(",")[0][2:-1]: float(s[:-2].split(",")[1])})
    fname.close()

    s=sorted(text.items(),key=lambda x:x[1],reverse=False)
    print(s)
    x_x=[]
    y_y=[]
    for i in s:
        x_x.append(i[0])
        y_y.append(i[1])
    plt.figure(figsize=(10,5))
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title(city+'加权平均',fontsize=20)
    plt.barh(x_x[-20:],y_y[-20:])
    plt.savefig('D:/data/weighted_rank/10/bar_'+city+'.png')
    # plt.show()