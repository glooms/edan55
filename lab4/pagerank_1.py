import re
import sys
import random

if len(sys.argv) != 3:
    sys.exit()

f = open(sys.argv[1], 'r')
r = int(sys.argv[2])
n = int(f.readline())
G = [[] for _ in range(n)]

for line in f:
    s = [int(i) for i in re.findall(r'\d+', line)]
    for i in range(0, len(s), 2):
        G[s[i]] += [s[i+1]]

print G

visited = [0] * n
state = 0
alpha = 0.85
for i in xrange(r):
    visited[state] += 1
    if len(G[state]) != 0 and random.random() < alpha:
        state = G[state][random.randint(0, len(G[state]) - 1)]
    else:
        state = random.randint(0, n - 1)

rf = map(lambda x: float(x)/r, visited)
print rf
