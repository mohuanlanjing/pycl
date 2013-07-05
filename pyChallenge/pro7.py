"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

import Image

img = Image.open('oxygen.png')
r,g,b,a = img.split()
x,y = img.size
l = []
for i in range(x):
    l.append(chr(r.getpixel(zip([i],[50])[0])))

l = l[::7]
print ''.join(l)

print ''.join([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]])


