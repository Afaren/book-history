#! /usr/bin/python
# coding=utf-8
import PIL
import jieba
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


import sys
default_encoding="utf-8"
if(default_encoding!=sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def wordcloudplot(txt):
    path = 'simhei.ttf'
    path = unicode(path, 'utf8').encode('gb18030')
    # background_image = 'timg.jpeg'
    # alice_mask = np.array(PIL.Image.open(background_image))
    wordcloud = WordCloud(font_path=path,
                          background_color="black",
                          margin=5, width=2100, height=1000,# mask=alice_mask,
                          max_words=2000,
                          max_font_size=130, random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('one_punch2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


f = open('tags_words.txt', 'r').read()
words = f.split('\n')

a = []
for w in words:
    if len(w) > 1:
        print(w)
        a.append(w)
txt = u' '.join(a)
print(u' '.join(a))
wordcloudplot(txt)
# print(txt)