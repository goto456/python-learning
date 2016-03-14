#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: init.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.10
#########################################################################

class Bird(object):
	def __init__(self):
		self.hungry = True
	
	def eat(self):
		if self.hungry:
			print 'Aaaah...'
			self.hungry = False
		else:
			print 'No thanks!'


class SongBird(Bird):
	def __init__(self):
		super(SongBird, self).__init__()
		self.sound = 'Squawk!'
	def sing(self):
		print self.sound
