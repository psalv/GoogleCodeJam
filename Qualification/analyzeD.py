

d1 = open('outD.txt', 'r')
# d1 = open('outDafter.txt', 'r')
# d2 = open('outDbefore.txt', 'r')
d2 = open('outD2.txt', 'r')
d3 = open('dif2.txt', 'w')

for line1 in d1:
    line2 = d2.readline()
    if line1 != line2:
        d3.write("After: " + line1)
        d3.write("Before: " + line2)
        d3.write("\n")
d3.close()
