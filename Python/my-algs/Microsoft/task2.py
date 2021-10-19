
def solution(S, C):
    startSeq=0
    endSeq=1
    seqLetter=S[0]
    cost=0
    index=1
    while index<len(C):
        if S[index]==seqLetter:
            endSeq+=1
        else:
            cost += delSeq(startSeq, endSeq, C)
            #print(locals())

            seqLetter=S[index]
            startSeq=index
            endSeq=index+1
        index+=1
        #print(locals())

    cost += delSeq(startSeq, endSeq, C)
    return cost


def delSeq(startSeq, endSeq, C):
    if endSeq - startSeq > 1:
        return sum(C[startSeq:endSeq]) - max(C[startSeq:endSeq])
    else:
        return 0





if __name__=='__main__':
    import doctest
    doctest.testfile('test2.txt')
    #doctest.testmod(verbose=True)