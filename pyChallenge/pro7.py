"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

import Image
import os

img = Image.open('oxygen.png')
#print os.linesep.join(dir(img))
r,g,b,a = img.split()
x,y = img.size
for i in range(x):
    for j in range(45, 55):
        print img.getpixel(zip([i],[j])[0])