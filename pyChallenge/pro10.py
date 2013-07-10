"""
http://www.pythonchallenge.com/pc/return/bull.html
a = [1, 11, 21, 1211, 111221,
"""
def say(num):
    l = len(num)
    slist = []
    i = 0
    ret = []
    while i<l:
        count = 1
        while i+1<l and num[i+1] == num[i]:
            count += 1
            i += 1
        slist.append({count:num[i]})
        i = i+1
    for i in slist:
        for key,value in i.items():
            ret.append(str(key)+value)
    return ''.join(ret)

def look_and_say(start):
    ret = [start]
    count = len(ret)
    while True:
        if count>30:
            break
        next = say(ret[-1])
        ret.append(next)
        count += 1
    return len(ret[30])

if __name__ == "__main__":
    print look_and_say('1')
