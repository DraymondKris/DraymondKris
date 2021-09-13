# encoding=utf-8

import math
import re
import jieba
import sys


# 从指定路径获取文本信息
def getfile(path):
    file = open(path, 'r', encoding='utf-8')
    message = file.read()
    file.close()
    return message


# 对字符串进行分割，分割规则：中文按词语分割，英文按单词分割，数字按空格分割，其中去掉标点符号
def cut(message):
    # 使用正则表达式去除标点符号，但是为了分割单词和数字，暂时保留空格
    comp = re.compile('[^A-Z^a-z0-9\u4e00-\u9fa5]')
    words = jieba.lcut(comp.sub('', message), cut_all=False)
    # 去掉空格
    word = [w for w in words if len(w.strip()) > 0]
    return word


# 对各词语出现次数进行统计
def count(text1, text2):
    #合并两个句子的单词
    key_word = list(set(text1 + text2))
    #统计句子一的词频，依次遍历key_word和text1,如果出现一样的词语，则+1
    vec1 = []
    for i in range(len(key_word)):
        vec1.append(0)
        for j in range(len(text1)):
            if key_word[i] == text1[j]:
                vec1[i] += 1
    #统计句子二的词频，依次遍历key_word和text2,如果出现一样的词语，则+1
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
    try:
        cos = (add / ((math.sqrt(squ1)) * (math.sqrt(squ2))))
        return cos
    except ZeroDivisionError:
        print('文本空白。')
        return 0


def main_test(path1, path2, save_path):
    try:
        file1 = getfile(path1)
        file2 = getfile(path2)
        cut1 = cut(file1)
        cut2 = cut(file2)
        count1, count2 = count(cut1, cut2)
        result = cosin(count1, count2)
        print(str(path1) + "与" + str(path2) + "的相似度：%.2f%%\n" % (result * 100))
        f = open(save_path, 'a', encoding="utf-8")
        f.write(str(path1) + "与" + str(path2) + "的相似度：%.2f%%\n" % (result * 100))
        f.close()
    # 捕捉文件路径错误
    except FileNotFoundError:
        print("抱歉，文件不存在。")


if __name__ == '__main__':
    filepath1 = ''
    filepath2 = ''
    result_save_path = ''
    try:
        # 与命令行参数交互
        filepath1 = sys.argv[1]
        filepath2 = sys.argv[2]
        result_save_path = sys.argv[3]
    except IndexError:
        filepath1 = input("输入原版文件路径:")
        filepath2 = input("输入抄袭版文件路径:")
        result_save_path = input("请输入要保存相似度结果的文件的路径：")
    main_test(filepath1, filepath2, result_save_path)
