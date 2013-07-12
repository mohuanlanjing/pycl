"""
http://www.pythonchallenge.com/pc/return/cat.html
"""

import calendar
for i in range(1006, 1997, 10):
    if calendar.isleap(i):
        if calendar.weekday(i, 1, 1) == 3:
            print i