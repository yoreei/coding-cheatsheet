from collections import deque
def deck_merge_sort(collection: list) -> list:
    """
    >>> deck_merge_sort([500, -100, 100, -50, 0, 50])
    [-100, -50, 0, 50, 100, 500]
    >>> deck_merge_sort([0, 1, 0, 1, 1])
    [0, 0, 1, 1, 1]
    >>> deck_merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> deck_merge_sort([])
    []
    >>> deck_merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list, right: list) -> list:
        #print(f'{left=}, {right=}, ', end='')
        def _merge():
            deck=deque()
            while left and right:
                deck.appendleft((left if left[-1] > right[-1] else right).pop())
            deck.extendleft(reversed(left))
            deck.extendleft(reversed(right))
            return deck

        result=list(_merge())
        #print(result)
        return result

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(deck_merge_sort(collection[:mid]), deck_merge_sort(collection[mid:]))

#----------------------------------------------------------------------------

def iter_merge_sort(input_list: list) -> list:
    """
    >>> iter_merge_sort([5, 9, 8, 7, 1, 2, 7])
    [1, 2, 5, 7, 7, 8, 9]
    >>> iter_merge_sort([6])
    [6]
    >>> iter_merge_sort([])
    []
    >>> iter_merge_sort([-2, -9, -1, -4])
    [-9, -4, -2, -1]
    >>> iter_merge_sort([1.1, 1, 0.0, -1, -1.1])
    [-1.1, -1, 0.0, 1, 1.1]
    """

    def iter_merge(merge_list: list, low: int, mid: int, high: int) -> list:
        result = []
        left, right = merge_list[low:mid], merge_list[mid: high + 1]
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        merge_list[low: high + 1] = result + left + right
        return merge_list

    if len(input_list) <= 1:
        return input_list

    # iteration for two-way merging
    size = 2
    while size < len(input_list):
        # getting low, high and middle value for merge-sort of single list
        for low in range(0, len(input_list), size):
            high = low + size - 1
            mid = (low + high + 1) // 2
            input_list = iter_merge(input_list, low, mid, high)
            #print(vars())
        # final merge of last two parts
        if size * 2 >= len(input_list):
            #print('yes')
            mid = low
            input_list = iter_merge(input_list, 0, mid, len(input_list) - 1)
        size *= 2

    return input_list

def topdown_list_sort(m: list):
    """
    >>> topdown_list_sort(deque([5, 9, 8, 7, 1, 2, 7]))
    deque([1, 2, 5, 7, 7, 8, 9])
    >>> topdown_list_sort(deque([6]))
    deque([6])
    >>> topdown_list_sort(deque([]))
    deque([])
    >>> topdown_list_sort(deque([-2, -9, -1, -4]))
    deque([-9, -4, -2, -1])
    >>> topdown_list_sort(deque([1.1, 1, 0.0, -1, -1.1]))
    deque([-1.1, -1, 0.0, 1, 1.1])
    """
    if len(m)<=1:
        return m

    left, right = deque(), deque()
    for i, x in enumerate(m):
        if i < len(m)/2:
            left.append(x)
        else:
            right.append(x)

    left = topdown_list_sort(left)
    right = topdown_list_sort(right)

    return list_merge(left, right)


def list_merge(left, right):
    result=deque()

    while left != deque() and right != deque():
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    while left != deque():
        result.append(left.popleft())
    while right != deque():
        result.append(right.popleft())
    return result

#--------------------------------------------
def topdown_array_sort(A:list, B:list, n):
    """
    >>> l=[5, 9, 8, 7, 1, 2, 7];topdown_array_sort(l, [0]*7, 7);l
    [1, 2, 5, 7, 7, 8, 9]
    >>> l=[6];topdown_array_sort(l,[0], 1);l
    [6]
    >>> l=[];topdown_array_sort(l, [], 0);l
    []
    >>> l=[-2, -9, -1, -4];topdown_array_sort(l, [0]*4, 4);l
    [-9, -4, -2, -1]
    >>> l=[1.1, 1, 0.0, -1, -1.1];topdown_array_sort(l, [0]*5, 5);l
    [-1.1, -1, 0.0, 1, 1.1]
    """
    arrcopy(A,B, n)
    topdown_splitmerge(B, 0, n, A)

def topdown_splitmerge(B:list, iBegin, iEnd, A:list):
    if iEnd - iBegin <= 1:
        return
    iMiddle = (iEnd + iBegin) // 2
    topdown_splitmerge(A, iBegin,  iMiddle, B)
    topdown_splitmerge(A, iMiddle,    iEnd, B)
    array_merge(B, iBegin, iMiddle, iEnd, A)

def bottomup_array_sort(A: list, B: list, n: int):
    """
    >>> l=[5, 9, 8, 7, 1, 2, 7];bottomup_array_sort(l, [0]*7, 7);l
    [1, 2, 5, 7, 7, 8, 9]
    >>> l=[6];bottomup_array_sort(l,[0], 1);l
    [6]
    >>> l=[];bottomup_array_sort(l, [], 0);l
    []
    >>> l=[-2, -9, -1, -4];bottomup_array_sort(l, [0]*4, 4);l
    [-9, -4, -2, -1]
    >>> l=[1.1, 1, 0.0, -1, -1.1];bottomup_array_sort(l, [0]*5, 5);l
    [-1.1, -1, 0.0, 1, 1.1]
    """

    width=1
    while width<n:
        i=0
        while i<n:
            array_merge(A, i, min(i + width, n), min(i + 2 * width, n), B)
            i+=2*width
        arrcopy(B, A, n)
        width*=2



def array_merge(A, iLeft, iRight, iEnd, B):
    """Used by both bottomup and topdown sorts"""

    j = iRight
    for k in range(iLeft, iEnd):
        if iLeft < iRight and (j >= iEnd or A[iLeft] <= A[j]):
            B[k] = A[iLeft]
            iLeft += 1
        else:
            B[k] = A[j]
            j += 1

def arrcopy(B, A, n):
    """Used by both bottomup and topdown sorts"""
    for i in range(0,n):
        A[i] = B[i]


if __name__ == "__main__":
    import doctest

    #l = [5, 9, 8, 7, 1, 2, 7];
    #bottomup_array_sort(l, [0] * 7, 7);
    #print(l)
    doctest.testmod(verbose=True)