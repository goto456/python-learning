#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtsleep4.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import threading
from time import sleep, ctime

sleep_time = [4, 2]

class ThreadFunc(object):
  def __init__(self, func, args, name=''):
    self.name = name
    self.func = func
    self.args = args

  def __call__(self):
    self.res = self.func(*self.args)

def loop(idd, time):
  print 'loop', idd, 'start at:', ctime()
  sleep(time)
  print 'loop', idd, 'done at:', ctime()

def main():
  print 'starting at:', ctime()
  threads = []
  num = len(sleep_time)
  
  for i in range(num):
    thread = threading.Thread(target=ThreadFunc(loop, (i, sleep_time[i]), loop.__name__))
    threads.append(thread)

  for i in range(num):
    threads[i].start()

  for i in range(num):
    threads[i].join()

  print 'all done at:', ctime()

if __name__ == '__main__':
  main()
  
