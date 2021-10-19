from collections import deque, Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# utility class to pass height object

class Height_Wrapper:
    """
    Used as a second return value for functions. Pass by reference
    """
    def __init(self):
        self.value = 0


def solution_util(root, height):
    """
    Returns 2 values. One in param _height_ and one as a return value
    :param height:  the height of the current node
    :return: the diameter of _root_
    """
    left_height = Height_Wrapper()
    right_height = Height_Wrapper()

    # root of recursion
    if root is None:
        height.value = 0
        return 0

    left_diam = solution_util(root.left, left_height)
    right_diam = solution_util(root.right, right_height)

    height.value = max(left_height.value, right_height.value) + 1

    # Formula for current diameter: left_height.value + right_height.value + 1
    return max(left_height.value + right_height.value + 1, max(left_diam, right_diam)) - 1


# function to calculate diameter of binary tree
def solution(root):
    """
    diameter of bin tree
    """
    height = Height_Wrapper()
    return solution_util(root, height)

if __name__=='__main__':
    import doctest
    doctest.testfile('test8.txt')
    doctest.testmod(verbose=True)
