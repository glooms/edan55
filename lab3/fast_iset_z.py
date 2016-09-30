import sys
import gmpy
import math

class MaxIset:
    n = 0      #Number of nodes in the graph
    G = []     #The graph
    c = 0

    
    def __init__(self):
        f = open(sys.argv[1], 'r')
        self.n = int(f.readline())
        self.G = [int(line.strip().replace(' ',''), base=2) for line in f]
        self.zs = [[i] for i in range(self.n)]
   
    def run(self):
        return self.r0(range(self.n), (1<<self.n) - 1)

    def add(self, v, V, mask):
        z_list = self.z_id(v)
        for z in z_list:
            V += [z]
            mask += (1<<(self.n - 1 - z))
        V.sort()
        return mask
 
    def remove(self, v, V, mask):
        z_list = self.z_id(v)
        for z in z_list:
            try:
                V.remove(z)
                mask -= (1<<(self.n - 1 - z))
            except: pass
#       mask = mask - 1<<(n - 1 - v)
        return mask


    def is_nb(self, v, u):
        return bool(self.G[v] & 1<<(self.n - 1 - u))


    def next_nb(self, v, mask):
        return self.n - 1 - int(math.log(self.G[v] & mask, 2))

    
    def z_id(self, v):
        return self.zs[v]

    def z_merge(self, u, w):
        self.zs[u] += [w]
        self.zs[w] += [u]

    def z_unmerge(self, u, w):
        self.zs[u].remove(w) 
        self.zs[w].remove(u) 
        
#TODO   Only the compound list of z is updated to be the union u and w.
#       Any node neighbouring w will not be update to now link to u,
#       making the graph faulty.
#       Could keep both elements in the vector V, skipping the larger of 
#       the two when looping and removing both if one is removed.
#       Then you need only keep track of which nodes are identical.
    def add_z(self, t, V, mask): # t is the tuple v, u and w
            (v, u, w) = t
            self.z_merge(u, w)
            z = self.G[u] | self.G[w]
            z -= 1<<(self.n - 1 - v)
            self.G += [self.G[u]]
            self.G[u] = z
            mask = self.add(u, V, mask)
            return mask
    

    def del_z(self, t):
        (v, u, w) = t
        self.z_unmerge(u, w)
        self.G[u] = self.G[-1:][0]
        self.G = self.G[:-1]

    def print_g(self, G):
        for r in G:
            print r

    def r0(self, V, mask, *flag):
        self.c += 1
        if not V:
            print 'This... is what\'s happening.'
            return 0
        m = -1
        max_deg = 0
#        print V
#        print bin(mask)[2:].zfill(self.n)
        for v in V:
            z_list = self.z_id(v)
            if len(z_list) > 1 and min(z_list) != v:
                continue
            s = gmpy.popcount(self.G[v] & mask) # - (1<<(self.n - 1 - v)))
            if s == 0:
                print 's: %d, v: %d' % (s, v)
                mask = self.remove(v, V, mask)
                return 1 + self.r0(V, mask)
            if s == 2: #R2
                mask = self.remove(v, V, mask)
                u = self.next_nb(v, mask)
                mask = self.remove(u, V, mask)
                w = self.next_nb(v, mask)
                mask = self.remove(w, V, mask)
                print 's: %d, v: %d, u: %d, w: %d' % (s, v, u, w)
                if self.is_nb(u, w):
                    return  1 + self.r0(V, mask)
                G = list(self.G)
                mask = self.add_z((v, u, w), V, mask)
                a = 1 + self.r0(V, mask)
                self.del_z((v, u, w))
                if G != self.G:
                    print 'Old G:'
                    self.print_g(G)
                    print 'New G:'
                    self.print_g(self.G)
                return a
            if s == 1: #R1
                print 's: %d, v: %d' % (s, v)
                mask = self.remove(v, V, mask)
                mask = self.remove(self.next_nb(v, mask), V, mask)
                return 1 + self.r0(V, mask)
            if s > max_deg:
                m = v
                max_deg = s
        print 's: %d, v: %d' % (max_deg, m)
        mask = self.remove(m, V, mask)
        a = self.r0(list(V), mask)
        V1 = list(V)
        for nb in V:
            if self.is_nb(m, nb):
                mask = self.remove(nb, V1, mask)
        return max(1 + self.r0(V1, mask), a)
         

   


#print n
#print V
#print mask

alg = MaxIset()
print alg.run()
print alg.c
