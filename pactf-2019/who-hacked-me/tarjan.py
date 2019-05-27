#!/usr/bin/env python3

# From http://stackoverflow.com/a/6575693/488265
# By http://stackoverflow.com/users/577088/senderle

from itertools import chain
from collections import defaultdict
import sys

class Graph(object):
    def __init__(self, edges, vertices=()):
        edges = list(list(x) for x in edges)
        self.edges = edges
        self.vertices = set(chain(*edges)).union(vertices)
        self.tails = defaultdict(list)
        for head, tail in self.edges:
            self.tails[head].append(tail)

    @classmethod
    def from_dict(cls, edge_dict):
        return cls((k, v) for k, vs in edge_dict.items() for v in vs)

class _StrongCC(object):
    def strong_connect(self, head):
        lowlink, count, stack = self.lowlink, self.count, self.stack
        lowlink[head] = count[head] = self.counter = self.counter + 1
        stack.append(head)

        for tail in self.graph.tails[head]:
            if tail not in count:
                self.strong_connect(tail)
                lowlink[head] = min(lowlink[head], lowlink[tail])
            elif count[tail] < count[head]:
                if tail in self.stack:
                    lowlink[head] = min(lowlink[head], count[tail])

        if lowlink[head] == count[head]:
            component = []
            while stack and count[stack[-1]] >= count[head]:
                component.append(stack.pop())
            self.connected_components.append(component)

    def __call__(self, graph):
        self.graph = graph
        self.counter = 0
        self.count = dict()
        self.lowlink = dict()
        self.stack = []
        self.connected_components = []

        for v in self.graph.vertices:
            if v not in self.count:
                self.strong_connect(v)

        return self.connected_components

strongly_connected_components = _StrongCC()

if __name__ == '__main__':
    sys.setrecursionlimit(500000) # avoid recursionerror
    with open('pwns.07737ac9d8bd.dat', 'r') as f:
        content = f.read().splitlines()
        content = [(f[7:23],f[-16:])  for f in content]
        # print(content[0])
        print(strongly_connected_components(Graph(content)))
    # edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
    #          ('E', 'A'), ('A', 'E'), ('C', 'A'), ('C', 'E'),
    #          ('D', 'F'), ('F', 'B'), ('E', 'F')]
    # print(strongly_connected_components(Graph(edges)))
    # edge_dict = {'a':['b', 'c', 'd'],
    #              'b':['c', 'a'],
    #              'c':['d', 'e'],
    #              'd':['e'],
    #              'e':['c']}
    # print(strongly_connected_components(Graph.from_dict(edge_dict)))