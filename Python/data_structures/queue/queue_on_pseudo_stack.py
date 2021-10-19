"""
!!! This is not any different than queue_on_list
Queue represented by a pseudo stack (represented by a list with pop and append)"""


class Queue:
    """
    >>> q=Queue(); q.put(1); q.put(2); q.put(3); str(q)
    '<1, 2, 3>'
    >>> q.get()
    1
    >>> str(q)
    '<2, 3>'
    >>> q.put(4); q.put(5); q.put(6); q.rotate(1); str(q)
    '<3, 4, 5, 6, 2>'
    >>> q.rotate(5); str(q)
    '<3, 4, 5, 6, 2>'
    >>> q.rotate(6); str(q)
    '<2, 3, 4, 5, 6>'
    >>> q.rotate(-1); str(q)
    '<4, 5, 6, 2, 3>'
    >>> q.rotate(-6); str(q)
    '<5, 6, 2, 3, 4>'
    """
    def __init__(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        printed = "<" + str(self.stack)[1:-1] + ">"
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item):
        self.stack.append(item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self):
        self.rotate(1)
        dequeued = self.stack[self.length - 1]
        self.stack = self.stack[:-1]
        self.rotate(self.length - 1)
        self.length = self.length - 1
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""

    def rotate(self, rotation):
        """
        Note that the direction is opposite from the one at collections.deque!
        :param rotation:
        :return:
        """
        for i in range(rotation):
            temp = self.stack[0]
            self.stack = self.stack[1:]
            self.length = self.length - 1
            self.put(temp)
            print(self.stack)

    """Reports item at the front of self
    @return item at front of self.stack"""

    def front(self):
        front = self.get()
        self.put(front)
        self.rotate(self.length - 1)
        return front

    """Returns the length of this.stack"""

    def size(self):
        return self.length

if __name__=="__main__":
    import doctest
    q=Queue()
    q.put(1);q.put(2);q.put(3);q.rotate(3);print(str(q))
    doctest.testmod(verbose=True)
