#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: socketserver.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.03.16
#########################################################################

from SocketServer import TCPServer, StreamRequestHander

class Hander(StreamRequestHander):
    
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting.')

server = TCPServer(('', 1234), Hander)
server.serve_forever()
