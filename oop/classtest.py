#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: classtest.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2015.12.30
#########################################################################

class AddrBookEntry(object):
	def __init__(self, nm, ph):
		self.name = nm
		self.phone = ph
		print 'Created instance for:', self.name
	def updatePhone(self, newph):
		self.phone = newph
		print 'Updated phone'

if __name__ == '__main__':
	addr_book_entry = AddrBookEntry('Aven', '88888')
	addr_book_entry.updatePhone(1234)
