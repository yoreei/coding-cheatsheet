from collections import defaultdict
import pprint


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
    """
    class Group(set):
        def __init__(self, *args, **kwargs):
            self.equilibrium=0
            self.update_equilibrium(args[0])
            super().__init__(*args, **kwargs)
        #def add(self, person):
        #    self.people.add(person)
        #    self.equilibrium+=P[person]-T[person]
        def update_equilibrium(self, ids:iter):
            for id in set(ids) - self:
                self.equilibrium+=P[id]-T[id]
                #print(f'{id=}, {self.equilibrium=}')
        def update(self, other:set):
            self.update_equilibrium(other)
            super().update(other)

    groups=[]
    bigGroup=set()
    for person1, person2 in zip(A, B):
        if {person1, person2} & bigGroup:
            match_ids=[]
            for group_id, group in enumerate(groups):
                if {person1, person2} & group:
                    match_ids.append(group_id)
                    group.update({person1, person2})
            unify_groups(groups, match_ids)

        else:
            newGroup=Group((person1, person2))
            groups.append(newGroup)

        bigGroup.update({person1, person2})

    #pprint.pprint(groups)
    return check_equilibrium(groups)

def unify_groups(groups: list, match_ids: list) -> None:
    united = groups[match_ids[0]]
    for id in match_ids[1:]:
        united.update(groups[id])
        del groups[id]

def check_equilibrium(groups):
    for group in groups:
        if group.equilibrium != 0:
            #print(f'{group=}, {group.equilibrium=}')
            return False
    return True




if __name__=='__main__':
    #P = [2, 2, 2, 2, 1, 1, 1, 1]
    #T = [1, 2, 2, 2, 1, 1, 1, 2]
    #A = [0, 0, 0, 0, 3]
    #B = [1, 2, 3, 4, 7]
    #solution(P, T, A, B)
    #breakpoint()


    import doctest
    doctest.testmod(verbose=False)