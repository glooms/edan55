import sys

call_count = 0

def r0(V, G):
    global call_count
    call_count += 1

    if not V:
        return 0
    u = -1
    max_deg = 0
    for v in V:
        s = 0
        n = []
        for i in V:
            s += G[v][i]
            if G[v][i]:
                n += [i]
        if s == 0:
            V.remove(v)
            return 1 + r0(V, G)
        if s == 1: #R1
            V.remove(v)
            V.remove(n[0])
            return 1 + r0(V, G)
        if s > max_deg:
            u = v
            max_deg = s
    V.remove(u)
    a = r0(list(V), G)
    V1 = list(V)
    for n in V:
        if G[u][n]:
            V1.remove(n)
    return max(1 + r0(V1, G), a)


f = open(sys.argv[1], 'r')
n = int(f.readline())
G = [[int(j) for j in line.strip().split(' ')] for line in f]
V = range(n)

print r0(V, G)
print call_count
