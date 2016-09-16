import sys


def r0(V):
    if not V:
        return 0
    u = -1
    max_deg = 0
    for v in V:
        s = 0
        for i in V:
            s = s + G[v][i]
        if s == 0:
            V.remove(v)
            return 1 + r0(V)
        if s > max_deg:
            u = v
            max_deg = s
    V.remove(u)
    a = r0(list(V))
    V1 = list(V)
    for n in V:
        if G[u][n]:
            V1.remove(n)
    return max(1 + r0(V1), a)


f = open(sys.argv[1], 'r')
n = int(f.readline())
G = []
for line in f:
    G = G + [[int(j) for j in line.strip().split(' ')]]

V = range(n)

print r0(V)
