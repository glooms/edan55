import sys
from tree import Node, Tree


def grparse():
    global G, n, m
    gr = open(file_name + '.gr')
    flag = False
    for line in gr:
        l = line.strip().split(' ')
        if l[0] == 'c':
            continue
        if not flag:
            (n, m) = map(int, l[-2:])
            flag = True
            G = [0] * (n)
        else:
            (i,j) = map(lambda x : int(x) - 1, l)
            G[i] += 1<<j
            G[j] += 1<<i

def tdparse():
    global B, T, b, w, v, root
    td = open(file_name + '.td')
    flag = False
    for line in td:
        l = line.strip().split(' ')
        if l[0] == 'c':
            continue
        if not flag:
            (b, w, v) = map(int, l[-3:])
            flag = True
            T = [[] for _ in xrange(b)]
            B = []
        else:
            if l[0] == 'b':
                bag = map(lambda x : int(x) - 1, l[1:])
                B += [(bag[0], bag[1:])]
            else:
                (i, j) = map(lambda x : int(x) - 1, l)
                T[i] += [j]
                T[j] += [i]
    for i in xrange(len(T)):
        if len(T[i]) == 1:
            root = i
            break
    if not root:
        root = 0
        
if len(sys.argv) != 2:
    sys.exit()

file_name = sys.argv[1].split('.')[0]
if file_name == 'gr-only':
    sys.exit()

G = [] # Graph
(n, m) = (0, 0) # nodes and egdes


B = [] # Bags
T = [] # Tree
(b, w, v) = (0, 0, 0) # # of bags, largest bag (width + 1), # of original vertices
root = '' 
grparse()
tdparse()
B.sort()
debug = 0

if not n:
    print 'Empty graph'
    sys.exit()

        
tree = Tree(root, B, T, G)
#tree.print_lvl_order()
#print
tree.post_order(tree.root, [])
print tree.max_i_set()

if not debug:
    sys.exit()

print '\n========PARSED INFO========\n'

print 'G'
for row in G:
    print bin(row)[2:].zfill(n)
print 'B'
for row in B:
    print row
print 'T'
for row in T:
    print row
