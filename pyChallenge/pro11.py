"""
http://www.pythonchallenge.com/pc/return/5808.html
"""
import Image
im = Image.open('cave.jpg')
w,h = im.size
l = []

o = e = Image.new(im.mode, (w/2, h/2))
for j in range(h):
    for i in range(w):
        if i%2 and j%2:
            o.putpixel(((i-1)/2,(j-1)/2), im.getpixel((i,j)))
        elif not i%2 and not j%2:
            e.putpixel((i/2,j/2), im.getpixel((i,j)))
o.show()
e.show()

    