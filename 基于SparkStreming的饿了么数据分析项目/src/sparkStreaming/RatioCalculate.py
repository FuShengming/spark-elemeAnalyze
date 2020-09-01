cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
# city="Beijing"
for city in cities:
    print(city)
    count=0
    fname = open('D:/data/recent_order_num/merge_'+city+'.txt', "rb")
    lines=[]
    while True:
        s=fname.readline()
        if s==b"":
            break
        s=str(s,encoding="utf-8")
        lines.append(s)
        print(s[:-2].split(",")[1])
        count+=int(s[:-2].split(",")[1])
    fname.close()
    fname = open('D:/data/recent_order_num/ratio_'+city+'.txt', "w")
    for line in lines:
        num=int(line[:-2].split(",")[1])
        s=line[:-2]+","+format(num/count,".8f")+")"
        print(s)
        fname.write(s+"\n")
    fname.close()

    count = 0
    fname = open('D:/data/shop_num/merge_'+city+'.txt', "rb")
    lines = []
    while True:
        s = fname.readline()
        if s == b"":
            break
        s = str(s, encoding="utf-8")
        lines.append(s)
        print(s[:-2].split(",")[1])
        count += int(s[:-2].split(",")[1])
    fname.close()
    fname = open('D:/data/shop_num/ratio_'+city+'.txt', "w")
    for line in lines:
        num = int(line[:-2].split(",")[1])
        s = line[:-2] + "," + format(num / count, ".8f") + ")"
        print(s)
        fname.write(s + "\n")
    fname.close()