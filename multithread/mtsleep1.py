#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtsleep1.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

import thread
from time import sleep, ctime

def loop0():
  print 'start loop 0 at:', ctime()
  sleep(4)
  print 'loop 0 done at:', ctime()

def loop1():
  print 'start loop 1 at:', ctime()
  sleep(2)
  print 'loop 1 done at:', ctime()
    
def main():
  print 'starting at:', ctime()
  thread.start_new_thread(loop0, ())
  thread.start_new_thread(loop1, ())
  sleep(6)
  print 'all done at:', ctime()

if __name__ == '__main__':
  main()
