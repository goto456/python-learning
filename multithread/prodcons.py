#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: prodcons.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.17
#########################################################################

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def writeQ(queue):
  print 'producing object in Q...'
  queue.put('xxx', 1)
  print 'size now:', queue.qsize()

def readQ(queue):
  print 'consumed object from Q...'
  val = queue.get(1)
  print 'size now:', queue.qsize()

def writer(queue, num):
  for i in range(num):
    writeQ(queue)
    sleep(randint(1, 3))

def reader(queue, num):
  for i in range(num):
    readQ(queue)
    sleep(randint(2, 5))
    
funcs = [writer, reader]
n = len(funcs)

def main():
  #num = randint(2, 5)
  num = 8
  q = Queue(32)

  threads = []
  for i in range(n):
    thread = MyThread(funcs[i], (q, num), funcs[i].__name__)
    threads.append(thread)

  for i in range(n):
    threads[i].start()

  for i in range(n):
    threads[i].join()

  print 'all done'

if __name__ == '__main__':
  main()
