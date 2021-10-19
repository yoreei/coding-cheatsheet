# This version uses object references instead of node indexes inside the children list.
# This approach is closer to the OOP solution with classes because we can now hop from node to
# node without having to go through the outer graph object every time. It's theoretically
# a cleaner solution because following a reference to an object is simpler than
# finding the object in a hashtable (dictionary) but it comes with a few caveats
# (I dare not say how much time I needed to make this one work)
#
# 1. How do we keep track of visited nodes during the algorithm and how
# do we compare nodes from the visited set to the current node? You can't add
# dictionaries to sets because dictionaries are mutable. We could use a list
# but this will degrade performance O(1) -> O(n)
# 1a. Comparing the id() of the nodes might work here, but will break if
# the algorithm deletes and adds nodes:
# https://docs.python.org/3/library/functions.html#id
# " Two objects with non-overlapping lifetimes may have the same id() value."
# 1b. The algorithm could mark the node by adding a new field, e.g. 'checked'
#  to see if the node has been seen before. This is not a bad solution, but has
# the following caveats:
# 1b I. Perhaps an algorithm is to be executed several times on the graph. You
# now have to remember to clean the marks every time before working on it. This
# is costly and adds one more place where you can make a mistake

# 1c. Solution: add an 'id' field in the node dictionary. Algorithms may add the id
# in their own sets for later comparison. The nodes are kept clean and the algorithms
# are easier to debug by printing locals()

# 2. Another gotcha is dictionary comparison. Since now we access node objects directly
# the node comparison code (x != fro) from graph_dict1 will crash. Python will try
# a deep comparison which will crash if the graph is circular.

# 3. The recursive nature of this solution makes it harder to debug using print().
# One has to from pprint import pprint and use the depth parameter

# Overall, I find this approach harder to work with.

import collections
from itertools import *
def parse(nodes1, nodes2, values):

    parsed = {} # could be a set or even a list]
    for node1, node2 in zip(nodes1, nodes2):
        if node1 not in parsed:
            parsed[node1] = {'c': [], 'id': node1}
        if node2 not in parsed:
            parsed[node2] = {'c': [], 'id': node2}

        parsed[node1]['c'].append(parsed[node2])
        parsed[node2]['c'].append(parsed[node1])  # comment out if directed

        parsed[node1]['v'] = values[node1]
        parsed[node2]['v'] = values[node2]

    return parsed

from pprint import pprint
def printqueue(queue):
    for fro, to in queue:
        print(f"{fro['id']=} {to['id']=}")

def local_circular(parsed, start):
    queue = collections.deque()
    queue.append((None, start))
    circle = set()
    while queue:
        fro, to = queue.pop()
        if to['id'] in circle:
            return True, circle
        else:
            circle.add(to['id'])
            children = zip(repeat(to), filter(lambda x: x is not fro, to['c']))
            queue.extend(children)
            #pprint(locals(), depth=3)
    return False, circle


def circular(nodes1, nodes2, values):
    parsed = parse(nodes1, nodes2, values)
    checked = set()
    for node in parsed.values():
        if node['id'] in checked:
            continue
        else:
            is_circ, loc_checked = local_circular(parsed, node)
            if is_circ:
                return True
            else:
                checked.update(loc_checked)
    return False

if __name__ == '__main__':
    print('circ')
    nodes1=[1,2,3,4]
    nodes2=[2,3,4,1]
    values=['_', 'c','d','d','d']
    ans = circular(nodes1, nodes2, values)
    assert ans == True, ans

    print('star')
    nodes1=[1,1,1,1]
    nodes2=[2,3,4,5]
    values=['_', 'c','d','d','d', 'c']
    ans = circular(nodes1, nodes2, values)
    assert ans == False, ans

    print('starcircle')
    nodes1=[1,1,1,4,5,6,7,8,9]
    nodes2=[2,3,4,1,6,7,8,9,1]
    values = ['c']*20
    ans = circular(nodes1, nodes2, values)
    assert ans == True, ans

    print('1circ')
    nodes1=[1,1,1,1,6,7,8]
    nodes2=[2,3,4,5,7,8,6]
    values = ['c']*20
    ans = circular(nodes1, nodes2, values)
    assert ans == True, ans

    print('2circ')
    nodes1=[1,2,3,4,5,6]
    nodes2=[2,3,1,5,6,4]
    values = ['c']*20
    ans = circular(nodes1, nodes2, values)
    assert ans == True, ans

    print('list')
    nodes1=[1,2,3,4]
    nodes2=[2,3,4,5]
    values = ['c']*20
    ans = circular(nodes1, nodes2, values)
    assert ans == False, ans

    print('tree')
    nodes1=[1,1,2,2,3,3,4,4]
    nodes2=[2,3,4,5,6,7,8,9]
    values = ['c']*20
    ans = circular(nodes1, nodes2, values)
    assert ans == False, ans
