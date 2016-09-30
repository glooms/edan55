import sys

call_count = 0

def add_z(v, u, w, V, old_G):
    z = []
    G = [list(row) for row in old_G]
    for i in range(len(G)):
        if G[i][u] or G[i][w]:
            G[i] += [1]
            z += [1]
        else:
            G[i] += [0]
            z += [0]
    z += [0]
    G += [z]
    V += [len(z) - 1]
    return G

def r0(V, G):
    global call_count
    call_count += 1

    if not V:
        print 'This... is what\'s happening.'
        return 0
    u = -1
    max_deg = 0
#    print V
    for v in V:
        s = 0
        n = []
        for i in V:
            s += G[v][i]
            if G[v][i]:
                n += [i]
        if s == 0:
            print 's: %d, v: %d' % (s, v)
            V.remove(v)
            return 1 + r0(V, G)
        if s == 2: #R2
            print 's: %d, v: %d, u: %d, w: %d' % (s, v, n[0], n[1])
            V.remove(v)
            V.remove(n[0])
            V.remove(n[1])
            if G[n[0]][n[1]]:
                return 1 + r0(V, G)
            new_G = add_z(v, n[0], n[1], V, G)
            return 1 + r0(V, new_G)
        if s == 1: #R1
            print 's: %d, v: %d' % (s, v)
            V.remove(v)
            V.remove(n[0])
            return 1 + r0(V, G)
        if s > max_deg:
            u = v
            max_deg = s
    print 's: %d, v: %d' % (max_deg, u)
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

print G[0]
print G[1]

print r0(V, G)
print call_count
