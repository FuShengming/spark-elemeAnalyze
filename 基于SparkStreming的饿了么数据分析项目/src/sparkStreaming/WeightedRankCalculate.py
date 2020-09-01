cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
# city="Beijing"
for city in cities:
    print(city)
    names=[]
    recent_order_nums=[]
    shop_nums=[]
    min_shop_num=5

    fname = open('D:/data/recent_order_num/merge_'+city+'.txt', "rb")
    while True:
        s=fname.readline()
        if s==b"":
            break
        s=str(s,encoding="utf-8")
        names.append(s.split(",")[0])
        recent_order_nums.append(int(s[:-2].split(",")[1]))
    fname.close()

    fname = open('D:/data/shop_num/merge_' + city + '.txt', "rb")
    while True:
        s = fname.readline()
        if s == b"":
            break
        s = str(s, encoding="utf-8")
        shop_nums.append(int(s[:-2].split(",")[1]))
    fname.close()

    # (WR) = (v / (v + m)) * R + (m / (v + m)) * C
    # v-销量 m-店铺数量下限 R-算术平均 C-总算数平均
    C=sum(recent_order_nums)/sum(shop_nums)

    fname = open('D:/data/weighted_rank/'+str(min_shop_num)+'/rank_'+city+'.txt', "w")
    for i in range(len(names)):
        if shop_nums[i]>=min_shop_num:
            WR=recent_order_nums[i]/(recent_order_nums[i]+min_shop_num)*(recent_order_nums[i]/shop_nums[i])+min_shop_num/(recent_order_nums[i]+min_shop_num)*C
            s = names[i] + ", " + format(WR, ".4f") + ")"
            fname.write(s + "\n")
    fname.close()
