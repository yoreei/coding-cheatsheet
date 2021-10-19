#from pprint import pprint
import heapq
from collections import deque

class Node:
    def __init__(self, arr_index, data):
        self.arr_index = arr_index
        self.data = data
        self.children=[]
    def __repr__(self):
        return f'{self.data} -> {self.children}'


def display(tree: Node) -> None:  # In Order traversal of the tree
    """
    """
    #print(tree.data, '->', tree.children)
    for child in tree.children:
        display(child)
def solution(S, A):
    if len(S) == 1:
        return 1

    nodes=[Node(i, S[i]) for i in range(len(S))]
    #pprint (nodes)
    for i in range(1, len(A)):
        nodes[A[i]].children.append(nodes[i])
        #print(locals())

    tasklist=deque([0])
    max_trees = []
    while tasklist:
        #print('----------newtask------')
        cur_node = nodes[tasklist.popleft()]
        cur_len=-find_length(cur_node, tasklist)
        #print(f'{cur_len=}')
        heapq.heappush(max_trees, cur_len)
    #print(max_trees)
    return abs(heapq.heappop(max_trees))

def find_length(node, next_nodes: deque):
    #print(f'{node=}')
    if node.children == []:
        #print('+1 has no children')
        return 1
    max_lengths = [] #[1]*len(node.children)
    some_children=False
    for index, child in enumerate(node.children):
        if child.data!=node.data:
            some_children=True
            #print('+1 in children')
            heapq.heappush(max_lengths, -1-find_length(child, next_nodes))
            #print(f'{max_lengths=}')
        else:
            next_nodes.append(child.arr_index)
    if some_children==False:
        #print('+1 unsuitable children')
        return 1

    smallest = heapq.nsmallest(2, max_lengths)
    if len(smallest)==2:
        return abs(sum(heapq.nsmallest(2, max_lengths)))-1
    else:
        return abs(sum(heapq.nsmallest(2, max_lengths)))

if __name__=='__main__':
    #root=solution('abbab', [-1, 0, 0, 0, 2])
    import doctest
    doctest.testfile('test3.txt')
    #doctest.testmod(verbose=True)