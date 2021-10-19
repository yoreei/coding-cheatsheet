
def solution(N):
    """
    >>> solution(9)
    2
    >>> solution(529) #1000010001
    4
    >>> solution(20) #10100
    1
    >>> solution(15) #1111
    0
    >>> solution(32) #100000
    0
    >>> solution(1041) #10000010001
    5
    >>> solution(1234) # 10011010010
    2
    """
    max_gap=0
    current_gap=0
    # 1. Remove right-trailing zeroes, e.g. 1010 -> 101
    while N%2==0:
        N=N>>1
    # 2. Find max gap
    while N>0:
        if N%2==1:
            max_gap = max(max_gap, current_gap)
            current_gap=0
        else:
            current_gap+=1
        N=N>>1
    return max_gap

if __name__=='__main__':
    import doctest
    doctest.testfile('tests.txt')
    #doctest.testmod(verbose=True)