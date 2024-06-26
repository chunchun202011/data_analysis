# -*- coding = utf-8 -*-
# @Time : 2023/6/13 20:15
# @Author:HUAWEI
# @File:testCloud.py
# @Software:PyCharm

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图，数据可视化
from wordcloud import WordCloud       # 词云
from PIL import Image                 # 图片处理
import numpy as np                    # 矩阵运算
import sqlite3                        # 数据库

# 准备词云所需的文字（词）
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
    # print(item[0])
# print(text)
cur.close()
con.close()


# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'static\assets\img\tree.jpg')  # 当前py所在文件目录下开始计算
img_arr = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask = img_arr,
    font_path = "simhei.ttf"
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴

# plt.show()  # 注：show和savefig不能同时执行

# 输出词云图片到文件
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)

