#coding: utf-8
"""
http://www.pythonchallenge.com/pc/return/balloons.html
"""

import difflib

f = file('delta.txt')

count = len(f.readline())
half = count/2
l2 = l1 = []
print f.readlines()
for i in f.readlines():
    print i
