#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtsleep2.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import thread
from time import sleep, ctime

sleep_time = [4, 2]

def loop(idd, sleep_time, lock):
  print 'start loop', idd, 'at:', ctime()
  sleep(sleep_time)
  print 'loop', idd, 'done at:', ctime()

def main():
  print 'starting at:', ctime()
  locks = []
  num = len(sleep_time)

  for i in range(num):
    lock = thread.allocate_lock()
    lock.acquire()
    locks.append(lock)

  for i in range(num):
    thread.start_new_thread(loop, (i, sleep_time[i], locks[i]))

  for i in range(num):
    while locks[i].locked():
      pass

  print 'all done at:', ctime()

if __name__ == '__main__':
  main()
    
