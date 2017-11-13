#! /usr/bin/python

import PIL
import jieba
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


def wordcloudplot(txt):
    path = 'simhei.ttf'
    path = unicode(path, 'utf8').encode('gb18030')
    background_image = 'timg.jpeg'
    alice_mask = np.array(PIL.Image.open(background_image))
    wordcloud = WordCloud(font_path=path,
                          background_color="white",
                          margin=5, width=1800, height=800, mask=alice_mask,
                          max_words=2000,
                          max_font_size=60, random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('one_punch2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


f = open('history.txt', 'r').read()
words = list(jieba.cut(f))
a = []
for w in words:
    if len(w) > 1:
        a.append(w)
txt = r' '.join(a)
wordcloudplot(txt)
