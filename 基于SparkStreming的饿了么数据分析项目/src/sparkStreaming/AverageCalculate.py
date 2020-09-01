cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
# city="Beijing"
for city in cities:
    print(city)
    fname = open('D:/data/recent_order_num/merge_'+city+'.txt', "rb")
    recent_order_nums=[]
    while True:
        s=fname.readline()
        if s==b"":
            break
        s=str(s,encoding="utf-8")
        print(s[:-2].split(",")[1])
        recent_order_nums.append(int(s[:-2].split(",")[1]))
    fname.close()

    fname1 = open('D:/data/shop_num/merge_'+city+'.txt', "rb")
    fname2 = open('D:/data/recent_order_num/avg_'+city+'.txt', "w")
    for i in range(len(recent_order_nums)):
        s = fname1.readline()
        if s == b"":
            break
        s = str(s, encoding="utf-8")
        n=recent_order_nums[i]/int(s[:-2].split(",")[1])
        s = s[:-2].split(",")[0] + "," + format(n,".2f") + ")"
        print(s)
        fname2.write(s + "\n")

    fname1.close()
    fname2.close()