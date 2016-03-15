#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: testiterator.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.14
#########################################################################

class TestIterator(object):
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

if __name__ == '__main__':
    ti = TestIterator()
    print list(ti)
