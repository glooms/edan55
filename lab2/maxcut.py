import io
import sys
from random import randint

for i in range(0, int(sys.argv[2])):

    f = open(sys.argv[1], 'r')
    n = int(f.readline().split(' ')[0])
    nodes = [0] * (n + 1)
    maxcut = 0
    for line in f :
        t = [int(i) for i in line.split()]
        if nodes[t[0]] == 0 :
            nodes[t[0]] = randint(1, 2)
        if nodes[t[1]] == 0 :
            nodes[t[1]] = randint(1, 2)
        if nodes[t[0]] != nodes[t[1]] :
            maxcut += t[2]
    print maxcut
