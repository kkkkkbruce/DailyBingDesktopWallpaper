#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################################
##                                                                       ##
## GnomeBingLockScreen                                                   ##
## Copyright (C) 2018 张泽平 (Randy Hoffman)                              ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see http://www.gnu.org/licenses/.   ##
##                                                                       ##
###########################################################################
##          Author: 张泽平 (Randy Hoffman)                                ##
## Website/Contact: https://github.com/zhangzp9970/                      ##
###########################################################################
import json
import os
import urllib.request
import datetime

HOME=os.path.expandvars('$HOME')+"/"#user home directory
pic_dir=HOME+"Pictures/Bing"#default dir
isdelete=True
delete_time=7

def load_config():#the load config function
	global HOME
	global pic_dir
	config_dir=HOME+".config/Bing"
	json_file=config_dir+"/"+"config.json"
	init_config={'Bing':{'dir':pic_dir,'delete':'True','time':'7','version':'1.0'}}
	if not os.path.exists(config_dir):#if directory not exist, mkdir
		os.makedirs(config_dir)
	if not os.path.exists(json_file):#if config file not exist, write the default configurations to the file
		with open(json_file,'w',encoding='utf-8') as f:
			json.dump(init_config,f,ensure_ascii=False,indent=4)
	with open (json_file,'r',encoding='utf-8') as f:#load configurations
		config_json=json.load(f)
	pic_dir=config_json['Bing']['dir']
	isdelete=config_json['Bing']['delete']
	delete_time=config_json['Bing']['time']
	if not os.path.exists(pic_dir):
		os.makedirs(pic_dir)

def download_and_apply():
	global HOME
	global pic_dir
	date=datetime.datetime.now().strftime('%Y-%m-%d')
	picture=pic_dir+"/"+date+".jpg"
	bing_json_file=HOME+".bing.json"
	json_url="https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"#where to get the json file
	bing_url="https://www.bing.com"#bing.com main domain
	if not os.path.exists(picture):
		#get the json file and hide the file
		urllib.request.urlretrieve(json_url,bing_json_file)
		#open the file and import json string
		with open(bing_json_file,"r",encoding='utf-8') as f:
			bing_json=json.load(f)
		url_append=bing_json['images'][0]['url']
		url=bing_url+url_append
		#get picture
		urllib.request.urlretrieve(url,picture)
		#change screen saver
		cmd="pcmanfm -w "+picture
		os.system(cmd)

def del_old_pic():
	global isdelete
	global delete_time
	global pic_dir
	day_s=datetime.datetime.now()-datetime.timedelta(days = delete_time)
	day=day_s.strftime('%Y-%m-%d')
	pic_del=pic_dir+"/"+day+".jpg"
	if isdelete == True:
		if os.path.exists(pic_del):
			os.remove(pic_del)

if __name__=='__main__':
	load_config()
	download_and_apply()
	del_old_pic()
