from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def get_mask():
    x,y=np.ogrid[:1000,:1000]
    mask=(x-500)**2+(y-500)**2>480**2
    mask=255*mask.astype(int)
    return mask

fontpath='C:/Windows/Fonts/汉真广标艺术字体.ttf'
min_shop_num=10

cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
for city in cities:
    text = {}
    fname = open('D:/data/weighted_rank/'+str(min_shop_num)+'/rank_'+city+'.txt', "r")
    while True:
        s = fname.readline()
        if s == "":
            break
        s = str(s)
        if s.split(",")[0][2:-1]!='其他快餐':
            text.update({s.split(",")[0][2:-1]: float(s[:-2].split(",")[1])})
    fname.close()
    wc = WordCloud(font_path=fontpath, background_color="white", mask=get_mask(),scale=6)
    wc.generate_from_frequencies(text)
    wc.to_file('D:/data/weighted_rank/'+str(min_shop_num)+'/wc_rank_' + city + '.png')
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    print("finish"+city)