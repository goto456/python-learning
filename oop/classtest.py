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

class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated email for:', self.name

if __name__ == '__main__':
    #addr_book_entry = AddrBookEntry('Aven', '88888')
    #addr_book_entry.updatePhone(1234)

    empl = EmplAddrBookEntry("Aven", 88888, 123, 'xxx@qq.com')
    print empl.email
    print empl.phone
    empl.updateEmail("234@qq.com")
    empl.updatePhone(999999)
    print empl.email
    print empl.phone
