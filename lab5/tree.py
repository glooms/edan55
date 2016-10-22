import gmpy

class Tree:
    def __init__(self, root, B, T, G):
        self.root = Node(B[root])
        Node.G = G
        self.B = B
        self.T = T
        self.table = [[] for _  in xrange(len(B))]
        self.make_tree(self.root, -1)
    
    def make_tree(self, node, p_index):
        for t in self.T[node.index]:
            if p_index != t:
                child = Node(self.B[t])
                if child.index != node.index:
                    node.children += [child]
        for c in node.children:
            self.make_tree(c, node.index)
   
    def max_i_set(self):
        pair = max(self.table[self.root.index])
        return (pair[0], translate(pair[1]))

    def print_lvl_order(self):
        string = self.level_order(self.root, [''] * len(self.T), 0)
        for s in string:
            if s:
                print s

    def level_order(self, node, s, i):
        s[i] += '(' + str(node.index) + ', '
        s[i] += str(node.vertices) + '): ' 
        s[i] += str([c.index for c in node.children]) + ' '
        i += 1
        for c in node.children:
            self.level_order(c, s, i)
        return s

    def post_order(self, node):
        for c in node.children:
            self.post_order(c)
        i_sets = node.i_sets()
        if not node.children:
            self.table[node.index] = i_sets
            return
        for U in i_sets:
            c_sum = [0, 0]
            for c in node.children:
                temp = []
                UcVt = U[1] & c.Vt
                for Ui in self.table[c.index]:
                    if Ui[1] & node.Vt == UcVt:
                        wU = Ui[0] - gmpy.popcount(Ui[1] & U[1])
                        temp += [(wU, Ui[1] - (Ui[1] & U[1]))]
                if temp: 
                    t = max(temp)
                    c_sum[0] += t[0]
                    c_sum[1] += t[1]
            self.table[node.index] += [(U[0] + c_sum[0], U[1] + c_sum[1])]
        return

class Node:
    G = []

    def __init__(self, (index, vertices)):
        self.index = index
        self.vertices = vertices
        self.Vt = sum(map(lambda x : 1<<x, vertices))
        self.table = []
        self.children = []

    def i_sets(self):
        if not self.vertices:
            return []
        sets = [(0, 0)]
        w = len(self.vertices)
        for i in xrange(1, 1<<w): # xrange is non-inclusive
            t = i
            j = 0
            mask = 0
            ind = True 
            while t:
                if t & 1:
                    mask += 1<<self.vertices[j]
                    if self.G[self.vertices[j]] & mask:
                        ind = False
                        break
                t >>= 1
                j += 1
            if ind:
                sets += [(gmpy.popcount(mask), mask)]
        return sets

def translate(mask):
    s = []
    t = mask
    j = 0
    while t:
        if t & 1:
            s += [j]
        t >>= 1
        j += 1
    return s
