"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""
import urllib2
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = '66831'
while True:
    newurl = url+num
    html = urllib2.urlopen(newurl)
    pattern = re.compile(r'\d+')
    try:
        num = pattern.findall(html.read())[0]
    except:
        print html.read()
        break
    print newurl
