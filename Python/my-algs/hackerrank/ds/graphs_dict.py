# You might think that collections.defaultdict will make the
# parsing easier because you would have to only create the
# nodes that actually have children. I think choosing defaultdict
# for this reason is not worth it, because of other disadvantages:
#
# 1. accessing nonexistent nodes won't give you any feedback
#   (you need the error to know that somethings wrong)
# 2. If while iterating on the dict you purposefully access
#   a nonexistent node, python will crash, because the dict
#   changed size during iteration. Sure, you can work around
#   that one too, but that means you traded code simplicity
#   in the algorithm for code simplicity in the parsing :(
import collections
from itertools import *
def parse(nodes1, nodes2, values):
    parsed={}
    for node1, node2 in zip(nodes1, nodes2):
        if node1 in parsed:
            parsed[node1]['c'].append(node2)
        else:
            parsed[node1] = {'c': [node2]}
        # START del if undirected
        if node2 in parsed:
            parsed[node2]['c'].append(node1)
        else:
            parsed[node2] = {'c': [node1]}
        parsed[node2]['v']=values[node2]
        # END del if undirected

        parsed[node1]['v']=values[node1]

    return parsed


def local_circular(parsed, start):
    queue = collections.deque()
    queue.append((None, start))
    circle = set()
    while queue:
        fro, to = queue.pop()
        if to in circle:
            return True, circle
        else:
            circle.add(to)
            children = zip(repeat(to), filter(lambda x: x!=fro, parsed[to]['c']))
            queue.extend(children)
            print(locals())
    return False, circle


def circular(nodes1, nodes2, values):
    parsed = parse(nodes1, nodes2, values)
    checked = set()
    for node in parsed:
        if node in checked:
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
