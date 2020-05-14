# with open("comment03.txt",'w',encoding='utf-8') as f:
#     print(f.write("hello"))
import re
import xlwt
import os
from snownlp import SnowNLP

def fileInput(file,name):
    try:
        with open('Input\\'+name+'.txt','w',encoding='utf-8') as f:
            f.write(file)
        return 1
    except:
        print('原始数据写入出现问题')
        return 0

def fileProcess(name):
    try:
        with open('Input\\'+name+'.txt', 'r', encoding='utf-8') as f:
            #天猫的规则
            # commentList = re.findall(r'(?<="rateContent":").*?(?=")', f.read())
            # f.seek(0, 0)
            # timeList = re.findall(r'(?<="rateDate":").*?(?=")', f.read())

            # 淘宝的规则
            commentList = re.findall(r'(?<="content":").*?(?=")', f.read())
            f.seek(0,0)
            timeList = re.findall(r'(?<="date":").*?(?=")', f.read())
            
            List = []
            List.append(commentList)
            List.append(timeList)
        return List
    except:
        print('数据清洗出现问题')
        return None

def fileOutput(list,name):
    if list is None:return 0
    try:
        with open('Output\\comment\\'+name+'.txt', 'w', encoding='utf-8') as f1:
            for i in range(0,len(list[0])):
                # print("{}:{}\t{}\n".format(i, list[0][i],list[1][i]))
                f1.write(list[0][i]+'\n')
        with open('Output\\date\\' + name + '.txt', 'w', encoding='utf-8') as f2:
            for i in range(0, len(list[1])):
                # print("{}:{}\t{}\n".format(i, list[0][i],list[1][i]))
                f2.write(list[1][i]+'\n')
        return 1
    except:
        print('清洗后写入出现问题')
        return 0

def CreatExcelFile(filename):
    workBook = xlwt.Workbook()
    workSheet = workBook.add_sheet('dataAnalysis')

    commentDirs = os.listdir('Output\\comment\\')
    dateDirs = os.listdir('Output\\date\\')
    # print(commentDirs)
    count = 0
    for name in commentDirs:
        with open('Output\\comment\\' + name, 'r', encoding='utf-8') as f1:
            with open('Output\\date\\' + name, 'r', encoding='utf-8') as f2:
                Date = f2.readlines()
                # print(Date[count])
                for line in f1.readlines():
                    count += 1
                    line = line.strip()
                    try:
                        date = Date[(count - 1) % 20].strip()
                    except:
                        print("发生角标越界，已忽略")

                    # 情感分析
                    try:
                        s = SnowNLP(line)
                        sy = s.sentiments
                    except:
                        print("分词为空，已忽略")
                    # 导入excel中
                    workSheet.write(count, 1, line)
                    workSheet.write(count, 0, date)
                    workSheet.write(count, 2, sy)
    workBook.save(filename+'.xls')







