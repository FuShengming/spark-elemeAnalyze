import matplotlib.pyplot as plt

text = {}
fname = open('D:/data/duck/shop_num.txt', "rb")
while True:
    s = fname.readline()
    if s == b"":
        break
    s = str(s, encoding="utf-8")
    text.update({s.split(",")[0][2:-1]: int(s[:-3].split(",")[1])})
fname.close()

s=sorted(text.items(),key=lambda x:x[1],reverse=False)
print(s)
x_x=[]
y_y=[]
for i in s:
    x_x.append(i[0])
    y_y.append(i[1])
explode=[0,0,0.1,0,0]
plt.figure(figsize=(7,7))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('鸭-销量',fontsize=15)
plt.axis('equal')
plt.pie(y_y,explode=explode,labels=x_x,autopct='%1.1f%%')
plt.savefig('D:/data/duck/shop_num.png')
# plt.show()