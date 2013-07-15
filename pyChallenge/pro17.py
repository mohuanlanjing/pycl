#coding: utf-8
"""
http://www.pythonchallenge.com/pc/return/romance.html
hint1 = is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
"""

import cookielib
import urllib2
import re
import bz2
import xmlrpclib
from urllib import unquote_plus, quote_plus

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
info = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php")
value = "12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"%value
l = []
while True:
    request = urllib2.Request(url)
    html = urllib2.urlopen(request)
    info = opener.open(url)
    pattern = re.compile(r'(?<=is\s)\d+')
    for i in cookie:
        l.append(i.value)
    try:
        value = pattern.findall(html.read())[0]
    except:
        break
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"%value 
print bz2.decompress(unquote_plus(''.join(l)))
string = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

sp = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print sp.phone('Leopold')
    
inform = 'the flowers are on their way'
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
headers = {'Cookie':'info='+quote_plus(inform)}
req = urllib2.Request(url, headers=headers)
print urllib2.urlopen(req).read()

