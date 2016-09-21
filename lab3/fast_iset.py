import sys

def remove(v, V, mask):
    V.remove(v)
    mask = mask - 1<<(n - 1 - v)
    return (V, mask)

def p(V, mask):
    print V
    print bin(mask)[2:].zfill(n)

def r0(V, mask):
    if not V:
        return 0
    u = -1
    max_deg = 0
    for v in V:
        s = bin(G[v] & mask).count('1')
        if s == 0:
            (V, mask) = remove(v, V, mask)
            return 1 + r0(V, mask)
        if s > max_deg:
            u = v
            max_deg = s
    (V, mask) = remove(u, V, mask)
    a = r0(list(V), mask)
    V1 = list(V)
    for nb in V:
        if G[u] & 1<<(n - 1 - nb) != 0:
            (V1, mask) = remove(nb, V1, mask)
    return max(1 + r0(V1, mask), a)


f = open(sys.argv[1], 'r')
n = int(f.readline())
G = [int(line.strip().replace(' ',''), base=2) for line in f]

V = range(n)
mask = 2**n - 1

print n
print V
print mask

print r0(V, mask)
