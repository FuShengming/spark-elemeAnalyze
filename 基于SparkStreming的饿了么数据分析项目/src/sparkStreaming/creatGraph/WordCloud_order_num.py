from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def get_mask():
    x,y=np.ogrid[:1000,:1000]
    mask=(x-500)**2+(y-500)**2>480**2
    mask=255*mask.astype(int)
    return mask

fontpath='C:/Windows/Fonts/汉真广标艺术字体.ttf'

cities=["Beijing","Chengdu","Guangzhou","Nanjing","Shenyang"]
for city in cities:
    text = {}
    fname = open('D:/data/recent_order_num/merge_' + city + '.txt', "rb")
    while True:
        s = fname.readline()
        if s == b"":
            break
        s = str(s, encoding="utf-8")
        if s.split(",")[0][2:-1]!='其他快餐':
            text.update({s.split(",")[0][2:-1]: int(s[:-2].split(",")[1])})
    fname.close()
    wc = WordCloud(font_path=fontpath, background_color="white", mask=get_mask(),scale=6)
    wc.generate_from_frequencies(text)
    wc.to_file('D:/data/wc_order_num_' + city + '.png')
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    print("finish"+city)
    # plt.show()

    '''
    font_path:string：可以修改生成词云的字体格式，传递字体的文件格式为OTF或者TTF，需要给出完整路径
    width,height: int，默认为400,200,画布的大小，即生成分辨率为(400,200)的图片
    prefer_horizontal:float，默认为0.9，代表文本横向排版出现的频率为0.9，垂直排版频率为0.1
    mask:nd-array or None，默认为None，默认词云会填充画布默认大小，若不是None，则默认画布大小将失效，遮罩的形状被mask取代。mask中全白区域将不会绘制词云，所以导入图片时注意该图片的背景必须为白色，而填充区域为其他颜色，可以利用ps抠图放在纯白的画布中。
    contour_width:float，设置词云边界宽度，默认为0，不画出词云边界线，当mask中填充部分的边界平滑时可以设置contour_width，否则不需要设置该参数，会产生锯齿。
    contour_color:'black'，边界线颜色，默认为黑色，当contour_width不为0时，设置本参数改变边界线颜色。
    scale:float，默认为1，按比例放大(>1)画布或者缩小(<1)
    min_font_size:int，默认为4，最小的字体大小
    max_font_size:int or None，默认为None，字体的最大样式
    font_step:int，默认为1，字体大小的步长，大于1时会加快运算，但可能会导致较大误差（以测试为准）
    max_words:number，默认为200，显示单词或者汉字最大的个数
    stopwords:为字符串集或者None，设置需要屏蔽的词（不会显示类似of the i etc.），若为None则会使用内置词集
    background_color:默认值'black'，画布背景色，默认为黑色
    mode:string：默认值'RGB' ，当参数为'RGBA'，其中A代表透明度，且'background_color'不为空时,背景为透明。
    relative_scaling"float：默认值'auto'，文字出现的频率与字体大小的关系，设置为1时词语出现的频率越高，其字体越大，默认为0.5。
    color_func:callable：默认为None，获取颜色函数，用户可以实现从图像中获取颜色，为None时使用内部默认颜色参数
    regexp:string or None：使用正则表达式来分隔输入的文本，当使用了generate_from_frequencies时本参数将被屏蔽
    collocations:bool：默认为True ，是否包括两个单词的搭配，当使用了generate_from_frequencies时本参数将被屏蔽
    colormap:string or marplotlib colormap：默认为'viridis' ，随机为每个词染色，本参数使用了'color_func'时将会被屏蔽
    normalize_plurals：bool 默认为True，是否移除词尾的s，尚未发现本参数的用途。
    repeat:bool，默认为False，是否重复单词或者短语，直到满足max_words和min_font_size，当文本内容较少时建议设置为真
    '''
