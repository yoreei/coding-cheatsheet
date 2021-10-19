from collections import deque, Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def solution_util(root, first, second, third):
    """
    biggest 3 nodes in Bin Tree
    """
    if (root is None):
        return

    if (root.data > first[0]):
        third[0] = second[0]
        second[0] = first[0]
        first[0] = root.data

    elif (root.data > second[0]):
        third[0] = second[0]
        second[0] = root.data

    elif (root.data > third[0]):
        third[0] = root.data

    solution_util(root.left, first, second, third)
    solution_util(root.right, first, second, third)

def solution(root):
    first = [float('-inf')]
    second = [float('-inf')]
    third = [float('-inf')]
    solution_util(root, first, second, third)
    print(first[0], second[0], third[0])

# Time: O(N)
# Space: O(1)

if __name__=='__main__':
    import doctest
    doctest.testfile('test7.txt')
    doctest.testmod(verbose=True)
