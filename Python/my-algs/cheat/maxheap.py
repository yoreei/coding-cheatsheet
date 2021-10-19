import heapq
def maxheapify(heap):
    """
    Transform list into a max heap, in-place, in O(len(heap)) time. Signs are inverted.
    """
    for i in range(len(heap)):
        heap[i]=-heap[i]
    heapq.heapify(heap)

def maxheappop(heap):
    """
    Pop the smallest item off the heap, maintaining the heap invariant
    """
    return -heapq.heappop(heap)
def maxheappush(heap, item):
    """
    Push item onto heap, maintaining the heap invariant
    """
    heapq.heappush(heap, -item)

def maxheappushpop(heap, item):
    """
    Push item on the heap, then pop and return the smallest item from the heap.

    The combined action runs more efficiently than maxheappush() followed by
    a separate call to maxheappop().
    """
    return -heapq.heappushpop(heap, -item)

def maxheapreplace(heap, item):
    """
    Pop and return the current smallest value, and add the new item. Returned may be < item
    """
    return -heapq.heapreplace(heap, -item)

def maxheapget(heap, idx):
    """
    Peek an element from the heap
    """
    return -heap[idx]
