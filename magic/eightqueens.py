#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: eightqueens.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.15
#########################################################################

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX - state[i]) in (0, nextY - i):
            return True
    return False

def queen(num, state):
    if len(state) == num - 1:
        for i in range(num):
            if not conflict(state, i):
                yield (i,)
    else:
        for i in range(num):
            if not conflict(state, i):
                for result in queen(num, state + (i,)):
                    yield (i,) + result
                
def queens(num=8, state=()):
    for i in range(num):
        if not conflict(state, i):
            if len(state) == num - 1:
                yield (i,)
            else:
                for result in queens(num, state + (i,)):
                    yield (i,) + result

if __name__ == '__main__':
    print list(queen(4, (1, 3, 0)))
    print list(queen(4, ()))
    print list(queens(4, ()))
    for solution in queens():
        print solution
