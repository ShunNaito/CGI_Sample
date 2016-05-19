#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ここから
import os
import cgi
if 'QUERY_STRING' in os.environ:
    query = cgi.parse_qs(os.environ['QUERY_STRING'])
else:
    query = {}
#ここまでおまじない

a = int(query['a'][0]) #データaを整数として読み込む
b = int(query['b'][0]) #データbを整数として読み込む

#出力
print "Content-Type:text/html"
print
print "%d + %d = %d" % (a, b, a+b)