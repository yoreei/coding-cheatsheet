from collections import deque
from itertools import *
def rev2idx(revkey:int, maxlen:int):
    return abs(revkey - maxlen+1)
#def poisonousPlantsNoStack(p):
#    """
#    >>> poisonousPlants(6, 5, 8, 4, 7, 10, 9)
#    2
#    """
#    # first run O(N)
#    if len(p) == 1:
#        return 1 # TODO check
#    queue = deque()
#    tick = reversed(p[1:-1])
#    tock = reversed(p[:-2])
#    rev_idxs = count(len(p)-1, -1)
#    for right_plant, left_plant, rev_idx in zip(tick, tock, rev_idxs):
#        if right_plant > left_plant:
#            queue.append(rev_idx)
def max(a,b):
    if a>b:
        print ("first one!")
        return a
    elif a<b:
        print ("second one!")
        return b
    else:
        print ("equal!")
        return a

def poisonousPlants(p):
    """
    >>> poisonousPlants([6, 5, 8, 4, 7, 10, 9])
    2
    >>> poisonousPlants([3,6,2,7,5])
    2
    >>> poisonousPlants([6, 5, 8, 7, 4, 7, 3, 1, 1, 10])
    2
    >>> poisonousPlants([1, 4, 7, 6, 2]) # used to be 2
    3
    >>> poisonousPlants([0,0,0,0])
    0
    >>> poisonousPlants([4,3,2,1])
    0
    >>> poisonousPlants([1,2,3,4])
    1
    >>> poisonousPlants([4, 3, 7, 5, 6, 4, 2])
    3
    >>> poisonousPlants([])
    0
    """
    maxdays=0
    stack = deque()
    for plant in p:
        day = 1

        while stack:
            stack_life, stack_plant = stack[-1]
            if plant > stack_plant:
                break
            else:
                d, _ = stack.pop()
                day = max(day, d+1) # WHY!?!?!?!?!?!?!?!?
        if not stack:
            day = 0
        maxdays = max(maxdays, day)
        stack.append((day, plant))

    return maxdays

def pp_dominik(p): # works!!!
    """
    >>> poisonousPlants([6, 5, 8, 4, 7, 10, 9])
    2
    >>> poisonousPlants([3,6,2,7,5])
    2
    >>> poisonousPlants([6, 5, 8, 7, 4, 7, 3, 1, 1, 10])
    2
    >>> poisonousPlants([1, 4, 7, 6, 2])
    3
    >>> poisonousPlants([0,0,0,0])
    0
    >>> poisonousPlants([4,3,2,1])
    0
    >>> poisonousPlants([1,2,3,4])
    1
    >>> poisonousPlants([4, 3, 7, 5, 6, 4, 2])
    3
    >>> poisonousPlants([])
    0
    """
    stack = deque()
    maxDays = 0

    for plant in p:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)
            #days = d + 1 # makes it behave like mine

        if not stack:
            days = 0

        maxDays = max(maxDays, days)
        stack.append((plant, days))

    return maxDays

def pp(p):

    """
    >>> pp([6, 5, 8, 4, 7, 10, 9])
    2
    >>> pp([3,6,2,7,5])
    2
    >>> pp([6, 5, 8, 7, 4, 7, 3, 1, 1, 10])
    2
    >>> pp([1, 4, 7, 6, 2])
    2
    >>> pp([0,0,0,0])
    0
    >>> pp([4,3,2,1])
    0
    >>> pp([1,2,3,4])
    1
    >>> pp([4, 3, 7, 5, 6, 4, 2])
    3
    >>> pp([])
    0
    >>> pp([1,1,0,0,1,1,9,9,-1,-1])
    2
    """
    maxdays=0
    stack=deque([])
    for plant in reversed(p):
        day=0
        while stack and plant < stack[-1]:
            stack.pop()
            day+=1
        maxdays=max(maxdays,day)
        stack.append(plant)
    return maxdays


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=False)

    doctest.testfile('pptests.txt')
