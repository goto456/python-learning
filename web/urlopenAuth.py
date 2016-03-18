#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: urlopenAuth.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.18
#########################################################################

import urllib2

LOGIN = 'wesc'
PASSWD = "you'llNeverGuess"
URL = 'http://localhost'

def handler_version(url):
    from urlparse import urlpase as up
    hdlr = urllib2.HTTPBasicAuthHandler()
