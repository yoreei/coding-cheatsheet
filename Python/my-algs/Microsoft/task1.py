
def solution(A):
    """
    Assuming that N is the length of the array!
    """
    if len(A)==1:
        return 1

    if len(A)==2:
        return 2

    max_switching=2
    current_switching=2
    even=A[0]
    odd=A[1]
    #for index, num in enumerate(A[2:]):
    #    if index%2==0:
    #        if num == even:
    #            current_switching+=1
    #        else:
    #            max_switching=max(max_switching, current_switching)
    #            current_switching=0
    #    else:
    #        if num == odd:
    #            current_switching+=1
    #        else:
    #            max_switching=max(max_switching, current_switching)
    #            current_switching=0
    index=2
    while index < len(A):
        num=A[index]
        if index%2==0:
            if num == even:
                #print('advancing')
                current_switching+=1
            else:
                #print('backward')
                max_switching=max(max_switching, current_switching)
                current_switching=0
                even=num
                index-=1
                continue
        else:
            if num == odd:
                #print('advancing')
                current_switching+=1
            else:
                #print('backward')
                max_switching=max(max_switching, current_switching)
                current_switching=0
                odd=num
                index-=1
                continue
        index+=1

    return max(max_switching, current_switching)


if __name__=='__main__':
    import doctest
    doctest.testfile('test1.txt')
   # doctest.testmod(verbose=True)