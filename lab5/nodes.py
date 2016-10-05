class Node:
    children = []

    def __init__(self, index, vertices):
        self.index = index
        self.vertices = vertices
        self.table = []
