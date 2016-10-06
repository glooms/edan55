import sys
from nodes import Node

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
            G = [[] for _ in xrange(n + 1)]
        else:
            (i,j) = map(int, l)
            G[i] += [j]
            G[j] += [i]

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
            T = [[] for _ in xrange(b + 1)]
            B = [[]]
        else:
            if l[0] == 'b':
                bag = map(int, l[1:])
                B += [Node(bag[0], bag[1:])]
            else:
                (i, j) = map(int, l)
                T[i] += [j]
                T[j] += [i]
    for i in xrange(len(T)):
        if len(T[i]) == 1:
            root = B[i]
            break
        
def make_tree(node, p_index):
    global B, T
    for t in T[node.index]:
        if p_index != t:
            node.children += [B[t]]
    for c in node.children:
        make_tree(c, node.index)

def print_tree(node, s, i):
    s[i] += str(node.index) + ': '
    s[i] += str([c.index for c in node.children]) + ' '
    i += 1
    for c in node.children:
        print_tree(c, s, i)
    return s 

if len(sys.argv) != 2:
    sys.exit()

file_name = sys.argv[1].split('.')[0]

G = [] # Graph
(n, m) = (0, 0) # nodes and egdes


B = [] # Bags
T = [] # Tree
(b, w, v) = (0, 0, 0) # # of bags, largest bag (width + 1), # of original vertices
root = '' 
grparse()
tdparse()
make_tree(root, 0)
string = print_tree(root, [''] * n, 0)

for s in string:
    if s:
        print s

if True:
    sys.exit()
print '========PARSED INFO========'

print 'G'
for row in G:
    print row
print 'B'
for row in B:
    print row
print 'T'
for row in T:
    print row


