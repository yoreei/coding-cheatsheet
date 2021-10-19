class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
from itertools import *


def height(root):
    max_depth = 0
    stack = [(root, max_depth)]
    #breakpoint()
    while stack:
        node, depth = stack.pop()
        children = filter(lambda x: x is not None, [node.left, node.right])
        children_depth = zip(children, repeat(depth + 1))
        list(map(stack.append, children_depth))
        max_depth = max(max_depth, depth)
        print(locals())

    return max_depth


def setup(t, arr):
    tree = BinarySearchTree()
    for i in range(t):
        tree.create(arr[i])

    root=tree.root
    print(height(root))
