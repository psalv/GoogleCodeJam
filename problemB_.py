
def greater(n, i):
    a = int(n[i])
    try:
        b = int(n[i + 1])
        return a > b
    except IndexError:
        return False

def below(n):
    a = int(n)
    return str(a - 1)

def checkTidy(n):
    for i in xrange(len(n)):
        if greater(n, i):
            return False
    return True

def findLastTidy(n):
    if checkTidy(n):
        return n

    for i in xrange(len(n)):
        if greater(n, i):
            num = below(n[i])
            if num == '0':
                r = ""
                for j in xrange(len(n) - 1):
                    r += '9'
                return r
            l = len(n[i + 1:])
            r = ""
            for j in xrange(l):
                r += '9'
            n = n[:i] + below(n[i]) + r

    return findLastTidy(n)


t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    res = findLastTidy(str(n))
    print "Case #{}: {}".format(i, res)
