class Tree:
    def __init__(self, root, B, T):
        self.root = Node(B[root])
        self.B = B
        self.T = T
        self.make_tree(self.root, 0)
    
    def make_tree(self, node, p_index):
        for t in self.T[node.index]:
            if p_index != t:
                child = Node(self.B[t])
                if child.index != node.index:
                    node.children += [child]
        for c in node.children:
            self.make_tree(c, node.index)
    

    def print_lvl_order(self):
        string = self.level_order(self.root, [''] * len(self.T), 0)
        for s in string:
            if s:
                print s

    def level_order(self, node, s, i):
        s[i] += str(node.index) + ': '
        s[i] += str([c.index for c in node.children]) + ' '
        i += 1
        for c in node.children:
            self.level_order(c, s, i)
        return s

    def post_order(self, node, l):
        for c in node.children:
            self.post_order(c, l)
        l += [node.index]
        return l

class Node:
    def __init__(self, (index, vertices)):
        self.index = index
        self.vertices = vertices
        self.table = []
        self.children = []
