#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: myThread.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import threading
from time import sleep, ctime

class MyThread(threading.Thread):
  def __init__(self, func, args, name=''):
    super(MyThread, self).__init__()
    self.name = name
    self.func = func
    self.args = args

  def getResult(self):
    return self.res

  def run(self):
    print 'starting', self.name, 'at:', ctime()
    self.res = self.func(*self.args)
    print self.name, 'done at:', ctime()
