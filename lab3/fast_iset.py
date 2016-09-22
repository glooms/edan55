import sys
import gmpy
import math

def remove(v, V, mask):
    V.remove(v)
#    mask = mask - 1<<(n - 1 - v)
    mask -= 1<<(n - 1 - v)
    return mask

def r0(V, mask):
    global call_count
    call_count += 1
    if not V:
        return 0
    u = -1
    max_deg = 0
    for v in V:
        s = gmpy.popcount(G[v] & mask)
        if s == 0: 
            mask = remove(v, V, mask)
            return 1 + r0(V, mask)
        if s == 1: #R1
            mask = remove(v, V, mask)
            nb = int(round(n - 1 - math.log(G[v] & mask, 2)))
            mask = remove(nb, V, mask)
            return 1 + r0(V, mask)
        if s > max_deg:
            u = v
            max_deg = s
    mask = remove(u, V, mask)
    a = r0(list(V), mask)
    V1 = list(V)
    for nb in V:
        if G[u] & 1<<(n - 1 - nb):
            mask = remove(nb, V1, mask)
    return max(1 + r0(V1, mask), a)


f = open(sys.argv[1], 'r')
n = int(f.readline())
G = [int(line.strip().replace(' ',''), base=2) for line in f]

V = range(n)
mask = 2**n - 1

#print n
#print V
#print mask

call_count = 0
print r0(V, mask)
print call_count
