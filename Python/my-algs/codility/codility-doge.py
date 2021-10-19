from collections import defaultdict
def solution(P, T, A, B):
    """
    >>> P = [1, 1, 2]
    >>> T = [2, 1, 1]
    >>> A = [0, 2]
    >>> B = [1, 1]
    >>> solution(P, T, A, B)
    True

    >>> P = [2, 2, 1, 1, 1]
    >>> T = [1, 1, 1, 2, 2]
    >>> A = [0, 1, 2, 3]
    >>> B = [1, 2, 0, 4]
    >>> solution(P, T, A, B)
    False

    >>> P = [1, 1, 2, 2, 1, 1, 2, 2]
    >>> T = [1, 1, 1, 1, 2, 2, 2, 2]
    >>> A = [0, 2, 4, 6]
    >>> B = [1, 3, 5, 7]
    >>> solution(P, T, A, B)
    False

    >>> P = [2, 2, 2, 2, 1, 1, 1, 1]
    >>> T = [1, 1, 1, 1, 2, 2, 2, 2]
    >>> A = [0, 1, 2, 3, 4, 5, 6]
    >>> B = [1, 2, 3, 4, 5, 6, 7]
    >>> solution(P, T, A, B)
    True
    >>> P = [2, 2, 2, 2, 1, 1, 1, 1]
    >>> T = [1, 2, 2, 2, 1, 1, 1, 2]
    >>> A = [0, 1, 2, 3, 4, 5, 6]
    >>> B = [1, 2, 3, 4, 5, 6, 7]
    >>> solution(P, T, A, B)
    True
    >>> P = [2, 2, 2, 2, 1, 1, 1, 1]
    >>> T = [1, 2, 2, 2, 1, 1, 1, 2]
    >>> A = [0, 0, 0, 0, 3]
    >>> B = [1, 2, 3, 4, 7]
    >>> solution(P, T, A, B)
    True
    >>> P = [1, 2, 2, 1, 1, 1, 2, 2]
    >>> T = [2, 2, 2, 2, 1, 1, 1, 1]
    >>> A = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]
    >>> B = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 4, 5, 6 ,7, 5, 6, 7, 6, 7, 7]
    >>> solution(P, T, A, B)
    True
    >>> P = [1, 1, 2, 2]
    >>> T = [1, 1, 2, 1]
    >>> A = []
    >>> B = []
    >>> solution(P, T, A, B)
    False
    >>> P = [1, 1, 2, 2]
    >>> T = [1, 1, 2, 2]
    >>> A = []
    >>> B = []
    >>> solution(P, T, A, B)
    True
    >>> P = [1, 1, 2, 2]
    >>> T = [1, 1, 2, 2]
    >>> A = [0, 1, 2]
    >>> B = [1, 2, 3]
    >>> solution(P, T, A, B)
    True
    >>> P = [1, 1, 2, 2]
    >>> T = [1, 1, 2, 1]
    >>> A = [0, 1, 2]
    >>> B = [1, 2, 3]
    >>> solution(P, T, A, B)
    False
    """
    # 1. Build network (social outcasts are to be dealt with later)
    network=defaultdict(set)
    for person, knows in zip(A, B):
        network[person].add(knows)
        network[knows].add(person)
    #print(network)

    # 2. Satisfied people are there merely to connect
    # 2.1. Unsatisfied outcasts means IMPOSSIBLE
    for index in range(len(P)):
        if P[index]==T[index]:
            prune_person(network, index)
        elif index not in network:
            return False
    #print(network)

    # 3. Kill matches, but unify their networks first
    for person, knows in list(network.items()):
        for other_person in knows:
            if T[person]!=T[other_person]:
                prune_person(network, person, other_person)
    #print(network)
    if not network:
        return True
    else:
        return False


def prune_person(network:dict, *people):
    for person in people:
        for knows in network[person]:
            network[knows].update(network[person] - {knows})
            network[knows]-={person}
            if not network[knows]:
                del network[knows]
        del network[person]


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=False)