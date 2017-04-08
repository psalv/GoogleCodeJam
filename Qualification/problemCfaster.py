import math

# Appending to a list is taking much too long since the list is enormous.

def findGap(stalls):
    ind = 0
    gap = stalls[1] - stalls[0]
    for i in xrange(1, len(stalls) - 1):
        if stalls[i + 1] - stalls[i] > gap:
            ind = i
    return ind


def findStall(n, k):
    stalls = []
    stalls.append(0)
    stalls.append(n + 1)


    L = None
    R = None
    for i in xrange(k):

        x = findGap(stalls)
        L = stalls[x]
        R = stalls[x + 1]
        I = int(math.floor((L + R) / 2))

        stalls.append(I)
        stalls.sort()

    return (I - L - 1, R - I - 1)


t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input().split()
    res = findStall(int(n[0]), int(n[1]))
    print "Case #{}: {} {}".format(i, max(res), min(res))

