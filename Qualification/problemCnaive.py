

def computeL(stalls, i):
    n = 0
    while i >= 0:
        if stalls[i] == 1:
            return n
        n += 1
        i -= 1
    return n

def computeR(stalls, i):
    n = 0
    while i < len(stalls):
        if stalls[i] == 1:
            return n
        n += 1
        i += 1
    return n


def findStall(n, k):

    stalls = []
    for i in xrange(n):
        stalls += [0,]

    while k > 0:

        mI = None
        mL = None
        mR = None
        for i in xrange(n):
            if stalls[i] == 0:
                L = computeL(stalls, i - 1)
                R = computeR(stalls, i + 1)

                if mI == None or min(L, R) > min(mL, mR):
                    mL = L
                    mR = R
                    mI = i

                elif min(L, R) == min(mL, mR) and max(L, R) > max(mL, mR):
                    mL = L
                    mR = R
                    mI = i

        stalls[mI] = 1
        k -=1

    return (mL, mR)



t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input().split()
    res = findStall(int(n[0]), int(n[1]))
    print "Case #{}: {} {}".format(i, max(res), min(res))

