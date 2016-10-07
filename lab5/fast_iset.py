import sys
import gmpy
import math

class MaxIset:
    n = 0      #Number of nodes in the graph
    G = []     #The graph
    c = 0

    
    def __init__(self):
        if True:
            f = open(sys.argv[1].split('.')[0] + '.gr', 'r')
            flag = False
            for line in f:
                l = line.strip().split(' ')
                if l[0] == 'c':
                    continue
                if not flag:
                    (self.n, m) = map(int, l[-2:])
                    flag = True
                    self.G = [0] * (self.n)
                else:
                    (i,j) = map(lambda x : int(x) - 1, l)
                    self.G[i] += 1<<(self.n - 1 - j)
                    self.G[j] += 1<<(self.n - 1 - i)
        else:
            f = open(sys.argv[1], 'r')
            self.n = int(f.readline())
            self.G = [int(line.strip().replace(' ',''), base=2) for line in f]
    
   
    def run(self):
        return self.r0(range(self.n), (1<<self.n) - 1)

    def add(self, v, V, mask):
        V += [v]
        V.sort()
        return mask + (1<<(self.n - 1 - v))
 
    def remove(self, v, V, mask):
        V.remove(v)
#       mask = mask - 1<<(n - 1 - v)
        return mask - (1<<(self.n - 1 - v))


    def is_nb(self, v, u):
        return bool(self.G[v] & 1<<(self.n - 1 - u))


    def next_nb(self, v, mask):
        return self.n - 1 - int(math.log(self.G[v] & mask, 2))

        
#TODO   Only the compound list of z is updated to be the union u and w.
#       Any node neighbouring w will not be update to now link to u,
#       making the graph faulty.
    def add_z(self, t, V, mask): # t is the tuple v, u and w
            (v, u, w) = t
            z = self.G[u] | self.G[w]
            z -= 1<<(self.n - 1 - v)
            self.G += [self.G[u]]
            self.G[u] = z
            mask = self.add(u, V, mask)
            return mask
    

    def del_z(self, t):
        (v, u, w) = t
        self.G[u] = self.G[-1:][0]
        self.G = self.G[:-1]

    def print_g(self, G):
        for r in G:
            print r

    def r0(self, V, mask, *flag):
        self.c += 1
        if not V:
            return 0
        m = -1
        max_deg = 0
#        print V
#        print bin(mask)[2:].zfill(self.n)
        for v in V:
            s = gmpy.popcount(self.G[v] & mask) # - (1<<(self.n - 1 - v)))
            if s == 0:
                mask = self.remove(v, V, mask)
                return 1 + self.r0(V, mask)
            '''if s == 2: #R2
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
                return a'''
            if s == 1: #R1
                mask = self.remove(v, V, mask)
                mask = self.remove(self.next_nb(v, mask), V, mask)
                return 1 + self.r0(V, mask)
            if s > max_deg:
                m = v
                max_deg = s
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
