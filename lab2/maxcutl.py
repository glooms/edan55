import io
import sys
import math
from random import randint

maxcuts = []

for i in range(0, int(sys.argv[2])):

    f = open(sys.argv[1], 'r')
    n = int(f.readline().split(' ')[0])
    k = math.ceil(math.log(n + 1, 2))
    nodes = [0] * (n + 1)
    maxcut = 0
    s = randint(0, 2 ** k - 1)
    j = 0
    for line in f:
        t = [int(i) for i in line.split()]
        if nodes[t[0]] == 0:
            j += 1
            nodes[t[0]] = (1 & bin(j & s).count('1')) + 1
        if nodes[t[1]] == 0:
            j += 1
            nodes[t[1]] = (1 & bin(j & s).count('1')) + 1
        if nodes[t[0]] != nodes[t[1]]:
            maxcut += t[2]
    maxcuts += [maxcut]

mean = sum(maxcuts) / int(sys.argv[2])


def std_dev(l, m):
    s = 0
    for i in l:
        s += (i - m) ** 2
    s = float(s)
    N = float(sys.argv[2])
    dev = math.sqrt(s / (N - 1))
    return dev

dev = std_dev(maxcuts, mean)

print (mean, dev)
print max(maxcuts)
print min(maxcuts)
