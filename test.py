import requests
import re
import time
import os
from random import *
import log
import threading
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
x = input()
data = requests.get(x,headers=headers)
print(data.request.headers)
dirname = re.findall('<title>(.*?)</title>',data.text)[-1]
urls = re.findall('<img src="(.*?)">',data.text)
if not os.path.exists(dirname):
    print(dirname)
    dirname = re.sub(r'[?#*!%$^/\\&()|]', '', dirname)
    diranme = dirname.replace(' – Telegraph',"")
    #dirname = re.sub(r'[ - Telegraph]', '', dirname)
    print(dirname)
    os.mkdir(dirname)
else:
    exit()
n = len(urls)
log.log(urls,x,dirname,data)
i = 0
for url in urls:
    i+=1
    y = uniform(0, 0.1)
    print(y)
    time.sleep(y)
    url = "https://telegra.ph" + url
    print(i, "/", n)
    jpg = requests.get(url, headers=headers)
    filename = str(i) + ".jpg"
    #filename = "/".split(url)[-1]
    with open(dirname + "/" + filename, "wb") as f:
        f.write(jpg.content)
'''
def daw(urls):
    i = 0
    urls1 = []
    urls2 = []
    urls3 = []
    urls4 = []
    i1 = []
    i2 = []
    i3 = []
    i4 = []
    for url in urls:
        i += 1
        i0 = i%4
        match i0:
            case 0:
                i1.append(i)
                urls1.append(url)
            case 1:
                i2.append(i)
                urls2.append(url)
            case 2:
                i3.append(i)
                urls3.append(url)
            case 3:
                i4.append(i)
                urls4.append(url)
    return [[urls1,i1],[urls2,i2],[urls3,i3],[urls4,i4]]

'''
#print(urls)

print("exiting")
exit()