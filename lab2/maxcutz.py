import io
import sys
import math
from random import randint

maxcuts = []

s = 0

while(True):
    f = open(sys.argv[1], 'r')
    n = int(f.readline().split(' ')[0])
    k = math.ceil(math.log(n + 1, 2))
    if s == 2 ** k:
        break
    nodes = [0] * (n + 1)
    maxcut = 0
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
    s += 1

mean = sum(maxcuts) / len(maxcuts)


def std_dev(l, m):
    s = 0
    for i in l:
        s += (i - m) ** 2
    s = float(s)
    N = float(len(maxcuts))
    dev = math.sqrt(s / (N - 1))
    return dev

dev = std_dev(maxcuts, mean)

print (mean, dev)
print max(maxcuts)
print min(maxcuts)
