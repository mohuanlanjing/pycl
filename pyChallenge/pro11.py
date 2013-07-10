"""
http://www.pythonchallenge.com/pc/return/5808.html
"""
import Image
im = Image.open('cave.jpg')
h,w = im.size
l = []

o = e = Image.new(im.mode, (w/2, h/2))
for i in range(h):
    for j in range(w):
        if j%2 and j%2:
            o.putpixel((i/2,j/2), im.getpixel((i,j)))
        elif not i%2 and not j%2:
            e.putpixel((i/2,j/2), im.getpixel((i,j)))
o.show()
e.show()


#for i in range(h):
#    for j in range(w):
#        l.append( im.getpixel((i,j)))
#l = l[0::2]
##for mode in l:
#new = Image.new(im.mode, im.size)
#count = 0
#for i in range(0,h/2):
#    for j in range(0,w/2):
#        new.putpixel((i,j),l[count])
#        count += 1
#new.show()
    