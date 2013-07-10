#coding: utf-8
"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""
#import string
print ''.join([i for i in ''.join([i.rstrip() for i in file('pro2.txt')]) if i.isalpha()])


#import os
#import string
#import collections
#sep = os.linesep
#st = ''.join(i.rstrip() for i in file('pro2.txt'))
#dic = collections.OrderedDict()
#for i in st:
#    dic[i] = dic.get(i,0)+1
#print dic
#average = len(dic)
#print ''.join([i for i in dic if dic[i]<average])


#import os
#import string
#sep = os.linesep
#f = file('pro2.txt','r')
#st = string.replace(f.read(), sep, '')
#list1 =  sorted([[i, st.count(i)] for i in set(st)], key=lambda x:x[1])
#list2 = [i for i in list1 if i[1]<average]
#print sorted([(i[0], st.index(i[0])) for i in list2], key=lambda x:x[1])