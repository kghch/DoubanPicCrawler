# -*- coding: utf-8 -*-

import urllib
import urllib2
import os
from bs4 import BeautifulSoup

url = ''

#url = 'https://www.douban.com/photos/album/1617100987/'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

html_doc = response.read()

soup = BeautifulSoup(html_doc, "lxml")

item = {}

pic_all = soup.findAll("div", {"class": 'photo_wrap'})
item['picUrl'] = []
item['picDesc'] = []

for pic in pic_all:
	item['picUrl'].append(pic.img['src'])
	item['picDesc'].append(pic.a['title'])

folder_name = "pic"

os.mkdir(folder_name)
os.chdir(folder_name)


di = zip(item['picUrl'], item['picDesc'])

for i in range(len(di)):
	each_pic = di[i]
	
	url = each_pic[0].replace("thumb", "photo")
	#url = each_pic[0].replace("thumb", "large")
	desc = each_pic[1][0:8]
	image = urllib.URLopener()  
	image.retrieve(url, str(i)  + ".jpg")
