"""
http://www.pythonchallenge.com/pc/return/italy.html
"""

import Image
im = Image.open('wire.png')
w,h = im.size
l1 = []
for j in range(h):
    for i in range(w):
        l1.append(im.getpixel((i,j))) #l1 contains all the pixels from im

l2 = [(i,i-1,i-1,i-2) for i in range(100, 1, -2)]
new = Image.new(im.mode, (100, 100))
x = 0
y = 0
for i in l2: # i = (100, 99, 99 ,98) ....
    count = 1 
    for j in i: 
        for k in range(j):
#            print (x,y)
            new.putpixel((x,y), l1.pop(0))
            if count == 1: # (x, y) -> (x+j-1, y) 
                x = x + 1
            if count == 2: # (x ,y) -> (x, y+j-1)
                y = y + 1
            if count == 3: # (x, y) -> (x-j+1, y)
                x = x - 1
            if count == 4: # (x, y) -> (x, y-j+1)
                y = y - 1
        if count == 1:
            x -= 1
        if count == 2:
            y -= 1
        if count == 3:
            x += 1
        if count == 4:
            y += 1
        count = count + 1
new.show()
        