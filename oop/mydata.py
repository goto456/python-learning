#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mydata.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2015.12.30
#########################################################################

class MyDataWithMethod(object):
    def printFoo(self):
        print "You invoked printFoo()"

if __name__ == '__main__':
    myData = MyDataWithMethod()
    myData.printFoo()
