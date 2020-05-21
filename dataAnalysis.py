#!/usr/bin/env python
# encoding: utf-8
'''
@author: ZYZ
@contact: 609924504zyz@gmail.com
@file: dataAnalysis.py
@time: 5/12/2020 23:13
@desc:
'''
import xlrd
import matplotlib
import matplotlib.pyplot as plt
import collections
import configparser

cp = configparser.RawConfigParser()
cp.read('Infor.conf')

matplotlib.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

data = xlrd.open_workbook(cp.get('taobao','name')+'.xls')
table = data.sheets()[0]
dateList = table.col_values(0,1,table.nrows)
syList = table.col_values(2,1,table.nrows)

def commentByDay():
    dateName = []
    count = []
    temp = list(set(dateList))
    temp.sort()
    dict = collections.OrderedDict()
    for i in temp:
        dict[i] = dateList.count(i)
    for k,v in dict.items():
        dateName.append(k)
        count.append(v)

        plt.figure(figsize=(50,8),dpi=80)

        x = range(len(dateName))
        bar = plt.bar(x,count,width=0.5,color='steelblue',edgecolor = 'black')
        # plt.plot(x,count,color='red')
        plt.xticks(x,dateName)
        plt.xticks(rotation=-30)
        for rect in bar:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
        plt.savefig('Image\\commentByDay.jpg')

def sentiment():
    poisitive = []
    negetive = []
    normal = []
    for i in syList:
        try:
            if i > 0.2 :
                poisitive.append(i)
            elif i< 0.2 and i > 0.1:
                normal.append(i)
            else:
                negetive.append(i)
        except:
            print('格式出现异常，已忽略')
    size = [len(poisitive),len(normal),len(negetive)]
    labels = ['好评','中评','差评']
    explode = (0.1,0,0)
    plt.pie(size,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False)
    plt.savefig('Image\\sentiment.jpg')

def perDayCommentSy():
    count = 0
    sydict = collections.OrderedDict()
    i = 0
    while(i<len(dateList)):
        for j in range(i,len(dateList)):
            if dateList[i] == dateList[j]:
                try:
                    count += syList[j]
                except:
                    print("格式出现异常，已忽略")
            else:
                count = count/float(j-i)
                sydict[dateList[i]] = count
                count = 0
                i = j-1
                break
        i += 1
    x = range(len(sydict))
    y = []
    date = []
    for k,v in sydict.items():
        y.append(v)
        date.append(k)
    plt.figure(figsize=(50, 8), dpi=80)
    plt.plot(x,y,color='red')
    plt.xticks(x,date)
    plt.xticks(rotation=-30)
    plt.savefig('Image\\perDayCommentSy.jpg')


# if __name__ == '__main__':
#     commentByDay()
#     sentiment()
#     perDayCommentSy()
