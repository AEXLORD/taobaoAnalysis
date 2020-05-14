import requests
import configparser
import re

cp = configparser.RawConfigParser()
cp.read('Infor.conf')

def crawlerTaobao(num):
    try:
        #天猫的格式
        # url = re.sub('currentPage=1','currentPage='+str(num),cp.get('taobao','url'))
        # 淘宝的格式
        url = re.sub('currentPageNum=1', 'currentPageNum=' + str(num), cp.get('taobao', 'url'))
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Cookie':cp.get('taobao','Cookie'),
            'referer':cp.get('taobao','referer'),
            'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
            'accept-encoding':'gzip, deflate, br',
            'accept':'*/*'
        }
        req = requests.get(url, headers=headers)
        print('状态码：{}'.format(req.status_code))
        return req.text
    except:
        print("获取淘宝页面出现异常")

