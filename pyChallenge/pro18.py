#coding: utf-8
"""
http://www.pythonchallenge.com/pc/return/balloons.html
"""

import difflib
import Image

f = file('delta.txt')
count = len(f.readline())
half = count/2
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
for i in f.readlines():
    l1.append(i[0:half].strip())
    l2.append(i[half:count].strip())

diff = difflib.ndiff(l1,l2)
for i in diff:
    if i[0] == '+':
        l3.append(i[1:].split())
    if i[0] == '-':
        l4.append(i[1:].split())
    if i[0] == ' ':
        l5.append(i[1:].split())

l3 = [[int(j,16) for j in i] for i in l3]
l4 = [[int(j,16) for j in i] for i in l4]
l5 = [[int(j,16) for j in i] for i in l5]
p1 = Image.new('P',(len(l3[0]),len(l3)))
p1.show()


f.close()
