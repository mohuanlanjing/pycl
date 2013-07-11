"""
http://www.pythonchallenge.com/pc/return/evil.html
"""
import Image
f = file("evil2.gfx",'rb')
content = f.read()
f.close()

for i in range(5):
    ret = file(r'pro12/%d.png'%i, 'wb+')
    ret.write(content[i::5])
    Image.open('pro12/%d.png'%i).show()
    ret.close()

  