import jieba

file=open("D:\\MLlib-homwork\\评论.txt","r",encoding='utf-8')
segfile=open("D:\\MLlib-homwork\\seg.txt","a",encoding='utf-8')
stopwords=['，','！','。','“','”','？','、','了','!','?',',','.',' ','很','太','得','的','地','呢']
for line in file:
    sent=line
    tempList=list(line)
    seg_list = jieba.cut(sent,cut_all=False)
    splitWords = [x for x in seg_list if x not in stopwords]
    segfile.writelines(' '.join(splitWords))
