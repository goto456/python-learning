#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtsleep5.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import threading
from time import sleep, ctime

#sleep_time = (4, 2)
sleep_time = [4, 2]

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

def loop(idd, time):
  print 'loop', idd, 'start at:', ctime()
  sleep(time)
  print 'loop', idd, 'done at:', ctime()

def main():
  print 'starting at:', ctime()
  threads = []
  num = len(sleep_time)

  for i in range(num):
    thread = MyThread(loop, (i, sleep_time[i]), loop.__name__)
    threads.append(thread)

  for i in range(num):
    threads[i].start()
    
  for i in range(num):
    threads[i].join()

  print 'all done at:', ctime()

if __name__ == '__main__':
  main()
