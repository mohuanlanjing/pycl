"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import zipfile
import re

z = zipfile.ZipFile('channel.zip','r')
zlist = z.namelist()
pattern = re.compile(r'\d+')
start = '90052'
s = zlist.index(start+'.txt')
while True:
    f = z.read(zlist[s])
    try:
        next = pattern.search(f).group()
        print next
    except:
        print f
        break
    s = zlist.index(next+'.txt')





