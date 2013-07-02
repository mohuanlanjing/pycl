#coding: utf-8
"""
http://www.pythonchallenge.com/pc/def/equality.html
"""
import string
import os
import re
f = file('pro3.txt','r')
st = string.replace(f.read(), os.linesep, '')
pattern = re.compile(r'(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])')
print ''.join(pattern.findall(st))
f.close()