# encoding=utf-8

import math
import re
import jieba


# 从指定路径获取文本信息
def getfile(path):
    file = open(path, 'r', encoding='utf-8')
    message = file.read()
    file.close()
    return message


# 对字符串进行分割，分割规则：中文按字分割，英文按单词分割，数字按空格分割，其中去掉标点符号
def cut(message):
    # 使用正则表达式去除标点符号，但是为了分割单词和数字，暂时保留空格
    comp = re.compile('[^A-Z^a-z\u4e00-\u9fa5]')
    words = jieba.lcut(comp.sub('', message), cut_all=True)
    # 去掉空格
    word = [w for w in words if len(w.strip()) > 0]
    return word


# 对各词语出现次数进行统计
def count(text1, text2):
    key_word = list(set(text1 + text2))
    vec1 = []
    for i in range(len(key_word)):
        vec1.append(0)
        for j in range(len(text1)):
            if key_word[i] == text1[j]:
                vec1[i] += 1
    vec2 = []
    for k in range(len(key_word)):
        vec2.append(0)
        for m in range(len(text2)):
            if key_word[k] == text2[m]:
                vec2[k] += 1
    return vec1, vec2


# 计算文本的余弦相似度
def cosin(vec1, vec2):
    add = 0
    squ1 = 0
    squ2 = 0
    for i in range(len(vec1)):
        add += vec1[i] * vec2[i]
        squ1 += vec1[i] ** 2
        squ2 += vec2[i] ** 2
    cos = (add / ((math.sqrt(squ1)) * (math.sqrt(squ2))))
    return cos


if __name__ == '__main__':
    path1 = input("输入原版文件路径:")
    path2 = input("输入抄袭版文件路径:")
    file1 = getfile(path1)
    file2 = getfile(path2)
    cut1 = cut(file1)
    cut2 = cut(file2)
    count1, count2 = count(cut1, cut2)
    result = cosin(count1, count2)
    print("文章相似度：%.2f" % result)
    save_path = input("请输入要保存相似度结果的文件的路径：")
    f = open(save_path, 'w', encoding="utf-8")
    f.write(str(path1) + "与" + str(path2) + "的相似度：%.2f" % result)
    f.close()
