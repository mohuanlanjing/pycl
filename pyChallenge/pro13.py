"""
http://www.pythonchallenge.com/pc/return/disproportional.html
"""

import xmlrpclib

sp = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print sp.system.listMethods()
print sp.system.methodHelp('phone')
print sp.system.methodSignature('phone')
print sp.phone('Bert')