class MyHeap():
    def __init__(self, l: iter):
        self.data=[]
        for elem in l:
            self.push(elem)

    def __repr__(self):
        return str(type(self))+repr(self.data)
    def getParent(idx):
        return (idx-1)//2

    def getFirstChild(idx):
        return (idx+1)*2-1

    def push(self, elem):
        self.data.append(elem)
        push_idx = len(self.data) - 1
        parent_idx = MyHeap.getParent(push_idx)
        while parent_idx>=0 and self.data[push_idx] > self.data[parent_idx]:
            self.data[push_idx], self.data[parent_idx] = self.data[parent_idx], self.data[push_idx]
            push_idx=parent_idx
            parent_idx=MyHeap.getParent(parent_idx)

    def max_index(self, *args):
        # print(locals())
        idxs = iter(args)
        max_idx=next(idxs)
        max_num=self.data[max_idx]
        for idx in idxs:
            if self.data[idx] > max_num:
                max_idx=idx
                max_num = self.data[idx]
        return max_idx

    def pop(self):
        heapmax = self.data[0]
        push_idx=0
        self.data[push_idx]=self.data.pop(-1)
        fc_idx = MyHeap.getFirstChild(push_idx)
        while fc_idx < len(self.data):
            children=[fc_idx]
            if fc_idx + 1 < len(self.data):
                children.append(fc_idx + 1)

            max_idx = self.max_index(push_idx, *children)
            if max_idx == push_idx:
                return heapmax
            else:
                self.data[push_idx], self.data[max_idx] = self.data[max_idx], self.data[push_idx]
                push_idx = max_idx
                fc_idx = MyHeap.getFirstChild(push_idx)
        return heapmax
    def num_children(self, idx):
        diff = min(len(self.data) - MyHeap.getFirstChild(idx), 2)
        return max(diff, 0)

def test_heap_class(heap):
    print(heap)
    for idx in range(len(heap.data)):
        fc = MyHeap.getFirstChild(idx)
        if fc >= len(heap.data):
            return
        children = [fc]

        if children[0] + 1 < len(heap.data):
            children.append(children[0] + 1)

        # print(locals())
        assert heap.max_index(idx, *children) == idx, heap.max_index(idx, *children)

def test_heap_primitive(heap):
    print(heap)
    idx = 0
    fc = idx * 2 + 1
    while fc < len(heap):

        # print(locals())
        assert maxheapget(heap, idx) >= maxheapget(heap, fc)
        if fc + 1 < len(heap):
            assert maxheapget(heap, idx) >= maxheapget(heap, fc + 1)
        idx += 1
        fc = idx * 2 + 1


# START MAXHEAP

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

#END MAXHEAP


from itertools import *
if __name__=='__main__':
    lists=[[1,7,6,5,2], [1,2,3,4,5,6,8],
        [8,6,4,3,2,1], [-1,-2,-3,-4],
        [-6,-5,-4,-3,-2,-1], [1,7,2,5,3,4],
        [8,8,1,1,2], [0,0,0,0,0],
        []]
    maxheapclasses = [MyHeap(l) for l in lists]
    [maxheapify(l) for l in lists]
    both = list(zip(lists, maxheapclasses))
    for primitive, klass in both:
        test_heap_primitive(primitive)
        test_heap_class(klass)
    for primitive, klass in both[:-1]:
        num1 = maxheappop(primitive)
        num2 = klass.pop()
        test_heap_primitive(primitive)
        test_heap_class(klass)
        assert num1 == num2, (num1, num2)
    for primitive, klass in both:
        maxheappush(primitive, 999)
        klass.push(999)
        test_heap_primitive(primitive)
        test_heap_class(klass)
    for primitive, klass in both:
        maxheappush(primitive, -999)
        klass.push(-999)
        test_heap_primitive(primitive)
        test_heap_class(klass)
    for primitive, _ in both:
        maxheappushpop(primitive, 1000)
        test_heap_primitive(primitive)
        maxheappushpop(primitive, -1000)
        test_heap_primitive(primitive)
        maxheappushpop(primitive, 3)
        test_heap_primitive(primitive)
    for primitive, _ in both:
        maxheapreplace(primitive, 0)
        test_heap_primitive(primitive)
        maxheapreplace(primitive, 1001)
        test_heap_primitive(primitive)
        maxheapreplace(primitive, -3)
        test_heap_primitive(primitive)

