def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
    """
    :param sorting:
    :param left:
    :param right:
    :return:
    >>> l=[1,1,1,1,1,1,0,0,6,5]; quick_sort_3partition(l, 0, len(l)-1); l
    [0, 0, 1, 1, 1, 1, 1, 1, 5, 6]
    >>> l=[5,1,3,4,2]; quick_sort_3partition(l, 0, 4); l
    [1, 2, 3, 4, 5]
    >>> l=[1,2,3]; quick_sort_3partition(l, 0, 2); l
    [1, 2, 3]
    >>> l=[]; quick_sort_3partition(l, 0, 0); l
    []
    >>> l=[3,2,4,1]; quick_sort_3partition(l, 0, 3); l
    [1, 2, 3, 4]
    """
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[right]
    #print(f'starting: {sorting[left:right+1]}, {pivot=}')
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
#    print(f'{i=}, {a=}, {b=}, {pivot=}')
#    print(f'resursion({sorting}, {left}, {a-1}')
#    print(f'resursion({sorting}, {b + 1}, {right}')
#    print('-'*10)
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)

def qs(l, left, right):
    if left >= right:
        return
    a=i=left
    b=right
    pivot=l[right]
    while i<=b:
        if l[i]<pivot:
            l[i], l[a] = l[a], l[i]
            a+=1
            i+=1
        elif l[i]>pivot:
            l[i], l[b] = l[b], l[i]
            b-=1
        else:
            i+=1
    qs(l, left, a-1)
    qs(l, b+1, right)

def quicksort_intuitive(l):
    """
    >>> l=[1,1,1,1,1,1,0,0,6,5]; quicksort_intuitive(l)
    [0, 0, 1, 1, 1, 1, 1, 1, 5, 6]
    >>> l=[5,1,3,4,2]; quicksort_intuitive(l)
    [1, 2, 3, 4, 5]
    >>> l=[1,2,3]; quicksort_intuitive(l)
    [1, 2, 3]
    >>> l=[]; quicksort_intuitive(l)
    []
    >>> l=[3,2,4,1]; quicksort_intuitive(l)
    [1, 2, 3, 4]
    """
    length=len(l)
    if length<=1:
        return l
    pivot=l[length//2]
    small, sorted, big = [], [], []
    for i in l:
        if i<pivot:
            small.append(i)
        elif i>pivot:
            big.append(i)
        else:
            sorted.append(i)
    return quicksort_intuitive(small)+sorted+quicksort_intuitive(big)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
