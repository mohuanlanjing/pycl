"""
http://www.pythonchallenge.com/pc/def/map.html
"""

l = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr
 gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """

import string
fr = string.ascii_lowercase
to = string.ascii_lowercase[2:]+string.lowercase[:2]
#fr = 'abcdefghijklmnopqrstuvwxyz'
#to = 'cdefghijklmnopqrstuvwxyzab'
trans = string.maketrans(fr, to)
print string.translate('map', trans)