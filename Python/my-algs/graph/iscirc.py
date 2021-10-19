from itertools import *
from types import SimpleNamespace as Node
from collections import defaultdict

def iscirc_hard(nodes1, nodes2):
    G=dict()
    for n1, n2 in zip(nodes1, nodes2):
        if {n1,n2} & G.keys() == {n1,n2} and n1 in n2.p:
            return True
        if n1 not in G:
            if n2 in G:
                G[n1]=Node(c={n2 | G[n2].c}, p={})
            else:
                G[n1]=Node(c={n2},p={})

        else:
            if n2 in G:
                G[n1].c.update({n2+G[n2].c})
            else:
                G[n1].c.update({n2})

     #   elif n2 not in G:
     #       G[n1].c.add(n2)
     #       G[n2] = Node(c={}, p={n1})
        #else:
        #    G[n1].c.update({n2}+G[n2].c)


def iscirc(nodes1, nodes2):
    """
    >>> iscirc([1,2,3,4],[2,3,4,1])
    True
    >>> iscirc([1,2,3,4],[2,3,4,5])
    False
    >>> iscirc([],[])
    False
    >>> iscirc([1,2,3,4,5,6],[11,22,33,5,6,4])
    True
    >>> iscirc([1,2,3,4,5,6],[2,3,1,5,6,4])
    True
    >>> iscirc([1],[1])
    True
    >>> iscirc([1,2,3,4,5,6,7,8],[11,22,33,44,55,66,77,8])
    True
    >>> iscirc([1,1,1,1,1],[2,3,4,5,6])
    False
    >>> iscirc([1,1,1,2,2,2,3,3,3],[11,12,13,21,22,23,33,33,33]) # tree
    False
    >>> iscirc([1,1,1,2,2,2,3,3,3,8,8,9,9],[11,12,13,21,22,23,33,33,33,81,82,91,92]) # trees
    False
    >>> iscirc([1,1,1,2,2,2,3,3,3,8,8,9,9],[11,12,13,21,22,23,33,33,33,81,82,91,9])
    True
    >>> iscirc([1,2,3,6,7,8,4,9],[2,3,4,7,8,9,6,1])
    True
    >>> iscirc([11,12,13,21,22,23,31,32,33,14,24,34],[12,13,14,22,23,24,32,33,34,21,31,11])
    True
    >>> iscirc([11,12,13,21,22,23,31,32,33,14,24],[12,13,14,22,23,24,32,33,34,21,31])
    False
    >>> iscirc([1,3],[2,2])
    False
    """
    G = defaultdict(lambda: Node(c=set(), p=set()))
    for n1, n2 in zip(nodes1, nodes2):

        forward_connections = {n2} | G[n2].c
        G[n1].c.update(forward_connections)
        for p in G[n1].p:
            G[p].c.update(forward_connections)

        backward_connections = {n1} | G[n1].p
        G[n2].p.update(backward_connections)
        for c in G[n2].c:
            G[c].p.update(backward_connections)
        # pprint(G)
        if n1 in G[n1].c:
            return True
    return False

from pprint import pprint
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
