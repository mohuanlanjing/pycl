"""
http://www.pythonchallenge.com/pc/def/peak.html
"""
import urllib2
import cPickle as pickle
import os
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
f = urllib2.urlopen(url).read()
f1 = pickle.loads(f)
print os.linesep.join([ ''.join([i[0]*i[1] for i in j]) for j in f1 ])