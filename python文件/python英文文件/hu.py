# 参考：https://www.cnblogs.com/zhaof/p/9242449.html

import requests
import re
import os

# 创建文件夹
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False

# 下载图片
def download_pic(url, path):
    try:
        pic = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        return False
    string = path + url[-9:]
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    print('【下载】' + url)

# 获取图片链接
def get_pic_url(url):
    html = requests.get(url).text
    pic_url = re.findall('"pic_url":"(.*?)",', html, re.S)
    for each in pic_url:
        each = each.replace('\\', '')
        download_pic(each, path)

# 获取图片链接
def get_pic_url(url):
    html = requests.get(url).text
    pic_url = re.findall('"pic_url":"(.*?)",', html, re.S)
    for each in pic_url:
        each = each.replace('\\', '')
        download_pic(each, path)

# 获取图片链接
def get_pic_url(url):
    html = requests.get(url).text
    pic_url = re.findall('"pic_url":"(.*?)",', html, re.S)
    for each in pic_url:
        each = each.replace('\\', '')
        download_pic(each, path)

# 获取图片链接
def get_pic_url(url):
    html = requests.get(url).text
    pic_url = re.findall('"pic_url":"(.*?)",', html, re.S)
    for each in pic_url:
        each = each.replace('\\', '')
        download_pic(each, path)

