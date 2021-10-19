def findSubSum(numbers, start, end):
    subsum = 0
    index = start
    zeroes = 0
    while index <= end:
        subsum += numbers[index]
        if numbers[index] == 0:
            zeroes += 1
        index += 1
    return (subsum, zeroes)


cache = {}
starts = []


def findSum(numbers, queries):
    sums = []
    for idx in range(0, len(numbers)):
        sums.append(findSubSum(numbers, 0, idx))
    print(sums)
    answers = []
    for query in queries:
        bigsubsum = sums[query[1] - 1]
        bigquery = bigsubsum[0] + bigsubsum[1] * query[2]
        print(bigquery)
        smallend = query[0]-2
        if smallend >= 0:
            smallsubsum = sums[query[0] - 1]
            smallquery = smallsubsum[0] + smallsubsum[1] * query[2]
        else:
            smallquery=0
        print(smallquery)
        ans = bigquery - smallquery
        answers.append(ans)
    return answers

if __name__=='__main__':
    print(findSum([5,10,10], [[1,2,5]]))

