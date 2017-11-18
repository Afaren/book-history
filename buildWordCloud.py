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

# 参考的是下面这个知乎回答的代码
# 你用 Python 做过什么有趣的数据挖掘/分析项目？ - 挖数的回答 - 知乎
# https://www.zhihu.com/question/28975391/answer/100796070
def wordcloudplot(words, targetFile):
    chineseFontFile = 'chinese-font/simhei.ttf'
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

def generateWordCloudFrom(file, wordCloudFile):
    with open(file, 'r') as tagsInput:
        tags = tagsInput.read().split('\n')
        validTagList = []
        for tag in tags:
            if len(tag) > 1:
                print(tag)  # 打印出来只是为了看是否乱码
                validTagList.append(tag)
        tagsText = u' '.join(validTagList)
        print(u' '.join(validTagList))  # 打印出来只是为了看是否乱码
        wordcloudplot(tagsText, wordCloudFile)


tagsFile = 'tags_words.txt'
targetFile = 'my-book-history-in-collage-word-cloud.jpg'
generateWordCloudFrom(tagsFile, targetFile)


