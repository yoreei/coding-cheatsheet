"""
Test that heapq.heappop() is O(1) while list.pop(0) is O(n)
"""
import heapq
from random import randrange
from timeit import timeit

def heapbench():
    for _ in range(0,100):
        heapq.heappop(h)
def listbench():
    for _ in range(0,100):
        l.pop(0)

for size in range(10_000, 1_000_000, 10_000):
    l=[randrange(0,1000) for _ in range(size)]
    h=l[:]
    #print(l)
    #print(h)
    heapq.heapify(h)
    time_heapbench = timeit(heapbench, number=10)
    time_listbench = timeit(listbench, number=10)
    print(f"{size=}, {time_heapbench=}, {time_listbench=}, {time_heapbench<time_listbench=}")

