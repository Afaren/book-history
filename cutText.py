from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

def wordcloudplot(txt):
    # print(txt)
    alice_mask = np.array(PIL.Image.open('one_punch.jpg'))
    wordcloud = WordCloud(background_color="white",
                          margin=5, width=1800, height=800,mask=alice_mask,max_words=2000,max_font_size=60,random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('one_punch2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


f=open('history.txt','r').read()
words=list(jieba.cut(f))
a=[]
for w in words:
    if len(w)>1:
        a.append(w)
txt=r' '.join(a)
wordcloudplot(txt)



