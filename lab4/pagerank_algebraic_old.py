import re
import sys

if len(sys.argv) != 3:
    sys.exit()

f = open(sys.argv[1], 'r')
r = int(sys.argv[2])
n = int(f.readline())
P = [[0] * n for _ in range(n)]

for line in f:
    s = [int(i) for i in re.findall(r'\d+', line)]
    for i in range(0, len(s), 2):
        P[s[i]][s[i + 1]] += 1

for i in xrange(len(P)):
    s = sum(P[i])
    if s != 0:
        P[i] = map(lambda x: float(x)/s, P[i])

p = [float(1)/n] * n

for _ in xrange(0, r):
    for j in range(n):
        temp = 0
        for i in range(n):
            temp += p[i] * P[i][j]
        p[j] = temp

rf = map(lambda x: float(x)/sum(p), p)
print rf
