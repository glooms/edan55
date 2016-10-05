import re
import sys

if len(sys.argv) != 3:
    sys.exit()


f = open(sys.argv[1], 'r')
r = int(sys.argv[2])
n = int(f.readline())
H = {}
alpha = 0.85
deg = [0] * n


for line in f:
    s = [int(i) for i in re.findall(r'\d+', line)]
    for i in range(0, len(s), 2):
        tup = (s[i], s[i + 1])
        if not tup in H:
            H[tup] = 0.0 
        H[tup] += 1
        deg[s[i]] += 1

new_H = []
for (i, j) in H:
    new_H += [(i, j, H[(i, j)] / deg[i])]
H = new_H

D = [0.0 if deg[i] else 1.0 / n for i in xrange(n)]

p = [1] + [0] * (n - 1)

l_H = len(H)
muls = 0

for _ in xrange(r):
    new_p = [0] * n
    for (i, j, a) in H:
        new_p[j] += p[i] * a
    d = 0
    for i in xrange(n):
        d += p[i] * D[i]
    p1 = sum(p) * (1-alpha)/n
    for i in xrange(n):
        new_p[i] = (new_p[i] + d) * alpha + p1
    count = 0
    for i in xrange(n):
        if abs(p[i] - new_p[i]) < 0.005:
            count += 1
    if count == n:
        break
    muls += l_H + 2 * n + 1
    p = new_p
    

# print [i for i in sorted(enumerate(p), key=lambda x : x[1])][:-6:-1]
# print p
print muls
