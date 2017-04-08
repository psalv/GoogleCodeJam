

# Change the solution to act iteratively to avoid the recursion depth limit
def solveFlip(s, k, n, prev):
    while True:
        if checkFlipped(s):
            return n
        index = findMostUnflipped(s, k)

        if index + k > len(s) - 1:
            index = len(s) - k

        if prev == index:
            return "IMPOSSIBLE"
        else:
            prev = index

        for i in xrange(k):
            s[index] = (s[index] + 1) % 2
            index += 1
        n += 1

def checkFlipped(s):
    for i in s:
        if i == 0:
            return False
    return True

def findMostUnflipped(s, k):
    max = 0
    maxIndex = -1
    cur = 0
    for j in xrange(len(s)):
        if s[j] == 0:
            cur += 1
        else:
            cur = 0

        if cur > max:
            maxIndex = j - cur + 1
            max = cur
    return maxIndex


def buildArray(s):
    x = []
    for i in xrange(len(s)):
        if s[i] == '+':
            x.append(1)
        else:
            x.append(0)
    return x

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input().split(" ")
    s = n[0]
    k = int(n[1])
    s = buildArray(s)
    x = solveFlip(s, k, 0, -1)
    print "Case #{}: {}".format(i, x)

