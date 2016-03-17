#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: mtfacfib.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

from myThread import MyThread
from time import sleep, ctime

def fib(x):
  if x < 2:
    return 1
  else:
    return fib(x - 1) + fib(x - 2)

def fac(x):
  if x < 2:
    return 1
  else:
    return x * fac(x - 1)

funcs = [fib, fac]
n = 35

def main():
  num = len(funcs)

  print '*** Single Thread'

  for i in range(num):
    print funcs[i].__name__, 'start at:', ctime()
    print funcs[i](n)
    print funcs[i].__name__, 'done at:', ctime()

  print '\n*** Multi Thread'

  threads = []
  for i in range(num):
    thread = MyThread(funcs[i], (n,), funcs[i].__name__)
    threads.append(thread)

  for i in range(num):
    threads[i].start()

  for i in range(num):
    threads[i].join()
    print threads[i].getResult()

  print 'all Done'

if __name__ == '__main__':
  main()
