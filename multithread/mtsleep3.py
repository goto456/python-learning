#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtsleep3.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import threading
from time import sleep, ctime

sleep_time = [4, 2]

def loop(idd, sleep_time):
  print 'start loop', idd, 'at:', ctime()
  sleep(sleep_time)
  print 'loop', idd, 'done at:', ctime()

def main():
  print 'starting at:', ctime()
  threads = []
  num = len(sleep_time)

  for i in range(num):
    thread = threading.Thread(target=loop, args=(i, sleep_time[i]))
    threads.append(thread)

  for i in range(num):
    threads[i].start()

  for i in range(num):
    threads[i].join()

  print 'all done at:', ctime()

if __name__ == '__main__':
  main()
