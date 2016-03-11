#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: exception.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.10
#########################################################################

x = raw_input('Enter the first number: ')
y = raw_input('Enter the second number: ')
try:
	print int(x) / int(y)
except ZeroDivisionError, e:
	print e
	print 'The second num can\'t be zero. '

