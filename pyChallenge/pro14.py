"""
http://www.pythonchallenge.com/pc/return/italy.html
"""

import Image
im = Image.open('wire.png')
w,h = im.size
l1 = []
for j in range(h):
    for i in range(w):
        l1.append(im.getpixel((i,j)))

l2 = [(i,i-1,i-1,i-2) for i in range(100, 1, -2)]
new = Image.new(im.mode, (100, 100))
top = 0
left = 0

for walk in l2:
    for i in walk:
        count = 1
        for j in range(i):
            pass

                
