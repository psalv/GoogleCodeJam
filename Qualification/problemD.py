


### If I ever figure out what's wrong with this question,
### I can optimize by using the formula that a positions are diagonal iff:
    # x1 - y1 = x2 - y2     OR     x1 + y1 = x2 + y2

# What I can do is group diagonals into dictionary entries,
# and then just query the entries whenever I need to check if a tile is addable.
# In a similar way, I can group all rows and columns into their own dictionary entries,
# based off of x and y coordinates.

# Can do a dict[x1 + y1].contains('+') or a dict[x].contains('+') for instance.
# Whenever a new item is added it will need to be added t it's appropriate dict entries.

def addablePlus(grid, x, y):
    tempY1 = y
    tempY2 = y
    tempX1 = x
    tempX2 = x
    for i in xrange(len(grid)):
        tempX1 += 1
        tempX2 -= 1
        tempY1 += 1
        tempY2 -= 1

        if tempY1 >= 0:

            if tempX1 >= 0:
                try:
                    if grid[tempX1][tempY1] in '+o':
                        return False
                except IndexError:
                    pass

            if tempX2 >= 0:
                try:
                    if grid[tempX2][tempY1] in '+o':
                        return False
                except IndexError:
                    pass

        if tempY2 >= 0:
            if tempX1 >= 0:
                try:
                    if grid[tempX1][tempY2] in '+o':
                        return False

                except IndexError:
                    pass

            if tempX2 >= 0:
                try:
                    if grid[tempX2][tempY2] in '+o':
                        return False
                except IndexError:
                    pass

    return True


def addableCross(grid, x, y):
    tempY1 = y
    tempY2 = y
    tempX1 = x
    tempX2 = x
    for i in xrange(len(grid)):
        tempX1 += 1
        tempX2 -= 1
        tempY1 += 1
        tempY2 -= 1

        if tempY1 >= 0:
            try:
                if grid[x][tempY1] in 'xo':
                    return False
            except IndexError:
                pass

        if tempY2 >= 0:
            try:
                if grid[x][tempY2] in 'xo':
                    return False
            except IndexError:
                pass

        if tempX1 >= 0:
            try:
                if grid[tempX1][y] in 'xo':
                    return False

            except IndexError:
                pass

        if tempX2 >= 0:
            try:
                if grid[tempX2][y] in 'xo':
                    return False
            except IndexError:
                pass

    return True


def addPlus(grid):
    flag = False
    for x in xrange(len(grid)):
        for y in xrange(len(grid)):
            if grid[x][y] == '.':
                if addablePlus(grid, x, y):
                    grid[x][y] = '+'
                    flag = True
    return flag


def addCross(grid):
    flag = False
    for x in xrange(len(grid)):
        for y in xrange(len(grid)):
            if grid[x][y] == '.':
                if addableCross(grid, x, y):
                    grid[x][y] = 'x'
                    flag = True
    return flag


def addCircle(grid):
    for x in xrange(len(grid)):
        for y in xrange(len(grid)):
            if grid[x][y] != 'o' and addableCross(grid, x, y) and addablePlus(grid, x, y):
                grid[x][y] = 'o'


def stylyzeA(grid):
    pl = True
    cr = True

    while pl or cr:
        pl = addPlus(grid)
        cr = addCross(grid)

    addCircle(grid)

    return grid


def stylyzeB(grid):
    pl = True
    cr = True

    addCircle(grid)

    while pl or cr:
        pl = addPlus(grid)
        cr = addCross(grid)

    addCircle(grid)

    return grid


def getStyle(n):
    style = 0
    vals = {'+': 1, 'x': 1, 'o': 2, '.': 0}
    for x in xrange(len(grid)):
        for y in xrange(len(grid)):
            style += vals[n[x][y]]
    return style

vals = {'+': 1, 'x': 1, 'o': 2, '.': 0}

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input().split()
    size = int(n[0])
    dif = int(n[1])

    # Building the grid
    grid = []
    for j in xrange(size):
        grid.append([])
    for g in grid:
        for h in xrange(size):
            g.append('.')
    for k in xrange(dif):
        place = raw_input().split()
        grid[int(place[1]) - 1][int(place[2]) - 1] = place[0]

    # print grid
    n1 = stylyzeA([row[:] for row in grid])
    n2 = stylyzeB([row[:] for row in grid])

    # print n
    output = ""
    style = 0
    num = 0

    if getStyle(n1) > getStyle(n2):
        n = n1
    else:
        n = n2

    for x in xrange(len(grid)):
        for y in xrange(len(grid)):
            style += vals[n[x][y]]
            if grid[x][y] != n[x][y]:
                output += "\n" + n[x][y] + " " + str(x + 1) + " " + str(y + 1)
                num += 1
    print "Case #{}: {} {}".format(i, style, num) + output
    # print "Case #{}: {} {}   Size: {}".format(i, style, num, size)




