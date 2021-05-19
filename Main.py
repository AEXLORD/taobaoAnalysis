#!/usr/bin/env python
# encoding: utf-8
'''
@author: ZYZ
@contact: 609924504zyz@gmail.com
@file: Main.py
@time: 5/9/2020 19:10
@desc:半自动淘宝商品评论抓取工具
'''
import taobao
import filePreRegular
import dataAnalysis as DA
import configparser
import time
import random

cp = configparser.RawConfigParser()
cp.read('Infor.conf')

#1
print('数据爬取开始')
print('-'*20)
for i in range(0,int(cp.get('taobao','pageNumber'))):
    filename = cp.get('taobao','name')+str(i)
    filePreRegular.fileInput(taobao.crawlerTaobao(i+1),filename)
    list = filePreRegular.fileProcess(filename)
    filePreRegular.fileOutput(list,filename)
    print("已爬取第{}页评论".format(i))
    time.sleep(random.randint(20,30))

# #2
# print('数据获取成功，开始生成报表')
# print('-'*20)
# filePreRegular.CreatExcelFile(cp.get('taobao','name'))
# print('报表生成成功，请在根目录下查看')
# print('-'*20)

# #3
# print('正在生成图表...')
# DA.commentByDay()
# DA.sentiment()
# DA.perDayCommentSy()
# print("图表生成成功！，请在Image文件夹下查看")
