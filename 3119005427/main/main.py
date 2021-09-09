# encoding=utf-8

import jieba
import math
import re
import collections

#从指定路径获取文本信息
def getfile(path):
    file=open(path,'r',encoding='utf-8')
    message=file.read()
    file.close()
    return message

#过滤掉标点符号和数字，仅对中文文本和英文单词进行查重分析
def guolv(str):
    comp=re.compile('[^A-Z^a-z^\u4e00-\u9fa5]')
    return comp.sub('',str)

#进行结巴分割
def cut(str):
    str=jieba.lcut(str,cut_all=False)
    return str
