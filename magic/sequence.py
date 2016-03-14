#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: sequence.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.14
#########################################################################

def checkIndex(key):
	if not isinstance(key, (int, long)):
		raise TypeError
	if key < 0:
		raise IndexError

class ArithmeticSequence(object):
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self, key):
		checkIndex(key)

		try:
			return self.changed[key]
		except KeyError:
			return self.start + key * self.step

	def __setitem__(self, key, value):
		checkIndex(key)

		self.changed[key] = value

if __name__ == '__main__':
	s = ArithmeticSequence(1, 2)
	print s[4]
	s[4] = 2
	print s[4]
	print s[5]
