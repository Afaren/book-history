#! /usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import sys
from wordcloud import WordCloud

# 这段是网上抄的，用于解决编码问题
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# 1. 重命名变量名，更加表意
# 2. 抽取目标文件名为函数参数
def wordcloudplot(words, targetFile):
    chineseFontFile = 'simhei.ttf'
    encodeFontFile = unicode(chineseFontFile, 'utf8').encode('gb18030')
    wordcloud = WordCloud(font_path=encodeFontFile,
                          background_color="black",
                          margin=5, width=2100, height=1000,
                          max_words=2000,
                          max_font_size=130, random_state=42)
    wordcloud = wordcloud.generate(words)
    wordcloud.to_file(targetFile)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


tagsFile = 'tags_words.txt'
targetFile = 'my-book-history-in-collage-word-cloud.jpg'

with open(tagsFile, 'r') as tagsInput:
    tags = tagsInput.read().split('\n')
    a = []
    for tag in tags:
        if len(tag) > 1:
            print(tag)
            a.append(tag)
    txt = u' '.join(a)
    print(u' '.join(a))
    wordcloudplot(txt, targetFile)

