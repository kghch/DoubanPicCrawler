# -*- coding: utf-8 -*-

import urllib
import urllib2
import os
from bs4 import BeautifulSoup

name_count = 0

def crawl_from_url(url):
	global name_count

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

	di = zip(item['picUrl'], item['picDesc'])

	for i in range(len(di)):
		each_pic = di[i]
		
		url = each_pic[0].replace("thumb", "photo")
		#url = each_pic[0].replace("thumb", "large")
		#desc = each_pic[1][0:8]
		image = urllib.URLopener()  
		image.retrieve(url, str(name_count)  + ".jpg")
		name_count = name_count + 1


first_url = 'http://www.douban.com/photos/album/155343624/'

request = urllib2.Request(first_url)
response = urllib2.urlopen(request)

html_doc = response.read()
soup = BeautifulSoup(html_doc, "lxml")

urls = soup.find("div", {"class": "paginator"}).find_all('a')

folder_name = "pic"
os.mkdir(folder_name)
os.chdir(folder_name)


crawl_from_url(first_url)

for i in range(len(urls)):
	url = urls[i]['href']
	crawl_from_url(url)

print "oo"




