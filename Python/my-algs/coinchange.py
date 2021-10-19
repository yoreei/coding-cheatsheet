import doctest
def solution(w, coins):
    """
    >>> solution(4, [2])
    1
    >>> solution(5, [2,3])
    1
    >>> solution(5, [1,2,3])
    5
    >>> solution(6, [1,2,3])
    7
    >>> solution(8, [1,3,5,7])
    6
    >>> solution(4, [1,2,3])
    4
    """
    mem=[[-1 for _ in coins] for _ in range(w+1)]
    return cc(coins, w, len(coins)-1, mem, [])
    #return cc(coins, w, len(coins)-1, mem)

#def cc(coins, w, i, mem):
def cc(coins, w, i, mem, used):

    if i<0 or w<0:
        #print(locals(), 0)
        return 0
    if w==0:
        #print(used+[coins[i]], locals(), 1)
        return 1
    if mem[w][i]!=-1:
        return mem[w][coins[i]]
    way1=cc(coins, w-coins[i], i, mem, used+[coins[i]])
    way2=cc(coins, w, i-1, mem, used)
    #print(f"{w=}, {{way1=}, {way2=}")
    mem[w][i]!=way1+way2
    #print(locals())
    return way1+way2


# this one is from https://www.techiedelight.com/coin-change-problem-find-total-number-ways-get-denomination-coins
def count(S, n, N, lookup=dict(), used=[]):
    """
    >>> count([2], 0, 4, dict())
    1
    >>> count([2,3], 1, 5, dict())
    1
    >>> count([1,2,3], 2, 5, dict())
    5
    >>> count([1,2,3], 2, 6, dict())
    7
    >>> count([1,3,5,7], 3, 8, dict())
    6
    >>> count([1,2,3], 2, 4, dict())
    4
    """
    #print(locals())
    # if the total is 0, return 1 (solution found)
    if N == 0:
        #print(used)
        return 1

    # return 0 (solution does not exist) if total becomes negative,
    # no elements are left
    if N < 0 or n < 0:
        return 0

    # construct a unique key from dynamic elements of the input
    key = (n, N)

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
        # Case 1. Include current coin `S[n]` in solution and recur
        # with remaining change `N-S[n]` with the same number of coins
        include = count(S, n, N - S[n], lookup, used+[S[n]])

        # Case 2. Exclude current coin `S[n]` from solution and recur
        # for remaining coins `n-1`
        exclude = count(S, n - 1, N, lookup, used)

        # assign total ways by including or excluding current coin
        lookup[key] = include + exclude

    # return solution to the current subproblem
    return lookup[key]


if __name__=='__main__':
    doctest.testmod(verbose=False)