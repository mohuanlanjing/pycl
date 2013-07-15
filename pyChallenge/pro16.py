"""
http://www.pythonchallenge.com/pc/return/mozart.html
"""

import Image

im = Image.open('mozart.gif')

w,h = im.size
pink = 195
l = list(im.getdata())
for i in range(0, w*h, w):
    index = l.index(pink, i)
    l[i:i+w] = l[index:i+w]+l[i:index]

im.putdata(l)
im.save('new_mozart.gif')
im.show()

