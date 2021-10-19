"""
Solution apparently copied from https://www.geeksforgeeks.org/next-greater-element/
Problem Definition:
Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the
right side of x in the array. Elements for which no greater element exist,
consider next greater element as -1.
"""
arr = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
expect = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, -1, -10, -5, -1, 0, -1]


def next_greatest_element_slow(arr: list) -> list:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.
    Maximum element present after the current one which is also greater than the
    current one.
    >>> next_greatest_element_slow(arr) == expect
    True
    """
    result = []
    for i in range(0, len(arr), 1):
        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        result.append(next)
    return result


def next_greatest_element_fast(arr: list) -> list:
    """
    Like next_greatest_element_slow() but changes the loops to use
    enumerate() instead of range(len()) for the outer loop and
    for in a slice of arr for the inner loop.
    >>> next_greatest_element_fast(arr) == expect
    True
    """
    result = []
    for i, outer in enumerate(arr):
        next = -1
        for inner in arr[i + 1 :]:
            if outer < inner:
                next = inner
                break
        result.append(next)
    return result


def next_greatest_element(arr: list) -> list:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.
    Maximum element present after the current one which is also greater than the
    current one.

    A naive way to solve this is to take two loops and check for the next bigger
    number but that will make the time complexity as O(n^2). The better way to solve
    this would be to use a stack to keep track of maximum number giving a linear time
    solution.
    >>> next_greatest_element(arr) == expect
    True
    >>> next_greatest_element([50,40,30,20,10])
    [-1, -1, -1, -1, -1]
    >>> next_greatest_element([10, 20, 30, 0, 40])
    [20, 30, 40, 40, -1]
    >>> next_greatest_element([10, -1, -20, 50, -50])
    [50, 50, 50, -1, -1]
    >>> next_greatest_element([10,5,100])
    [100, 100, -1]
    >>> next_greater_element2([0,0,0,0])
    [-1, -1, -1, -1]
    """
    stack = []
    result = [-1] * len(arr)

    for index in reversed(range(len(arr))):
        if len(stack):
            while stack[-1] <= arr[index]:
                stack.pop()
                if len(stack) == 0:
                    break

        if len(stack) != 0:
            result[index] = stack[-1]

        stack.append(arr[index])

    return result

def next_greater_element2(arr):
    """
    >>> next_greater_element2([50,40,30,20,10])
    [-1, -1, -1, -1, -1]
    >>> next_greater_element2([10, 20, 30, 0, 40])
    [20, 30, 40, 40, -1]
    >>> next_greater_element2([10, -1, -20, 50, -50])
    [50, 50, 50, -1, -1]
    >>> next_greater_element2([10,5,100])
    [100, 100, -1]
    >>> next_greater_element2([0,0,0,0])
    [-1, -1, -1, -1]
    """
    stack = []
    result = [0]*len(arr)

    for i in range(len(arr) - 1, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return result


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    #print(next_greatest_element_slow(arr))
    #print(next_greatest_element_fast(arr))
    #print(next_greatest_element(arr))

    #setup = (
    #    "from __main__ import arr, next_greatest_element_slow, "
    #    "next_greatest_element_fast, next_greatest_element"
    #)
    #print(
    #    "next_greatest_element_slow():",
    #    timeit("next_greatest_element_slow(arr)", setup=setup),
    #)
    #print(
    #    "next_greatest_element_fast():",
    #    timeit("next_greatest_element_fast(arr)", setup=setup),
    #)
    #print(
    #    "     next_greatest_element():",
    #    timeit("next_greatest_element(arr)", setup=setup),
    #)
