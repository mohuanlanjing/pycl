"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

from zipfile import ZipFile
import re
import os

z = ZipFile('channel.zip','r')
zlist = z.namelist()
pattern = re.compile(r'\d+')
start = '90052'
s = zlist.index(start+'.txt')
cmlist = [z.getinfo(start+'.txt').comment]
while True:
    f = z.read(zlist[s])
    try:
        next = pattern.search(f).group()
    except:
        break
    s = zlist.index(next+'.txt')
    cmlist.append(z.getinfo(next+'.txt').comment)

print ''.join(cmlist)
