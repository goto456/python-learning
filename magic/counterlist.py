#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: counterlist.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.14
#########################################################################

class CounterList(list):
	def __init__(self, *args):
		super(CounterList, self).__init__(*args)
		self.counter = 0

	def __getitem__(self, index):
		self.counter += 1
		return super(CounterList, self).__getitem__(index)
	
if __name__ == '__main__':
	cl = CounterList(range(10))
	print cl
	cl.reverse()
	print cl
	del cl[3: 6]
	print cl
	print cl.counter
	print cl[4] + cl[2]
	print cl.counter
