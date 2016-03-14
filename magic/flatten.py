#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: flatten.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.14
#########################################################################

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

def flatten2(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested


if __name__ == '__main__':
    nested = [[1, 2], [3, 4], [5]]
    for num in flatten(nested):
        print num

    nested = ['foo', ['bar', ['baz']]]
    print list(flatten2(nested))

