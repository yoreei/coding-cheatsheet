class Heap:
    """
    A generic Heap class, can be used as min or max by passing the key function
    accordingly.
    LIMITATIONS: This class is not meant to be used with items which have
    identical hash values, e.g.:
    h=Heap()
    h.insert_item(101,1)
    h.insert_item(102,2)
    h.insert_item(102,3)
    h.heappop()
    Out: [102, 3]
    h.heappop()
    Out: [102, 3]
    h.heappop()
    Traceback (most recent call last):
    ...
    KeyError: 102

    One may implement this feature by changing pos_map to be a dict of sets/lists
    """

    def __init__(self, key=None):
        # Stores actual heap items. arr[n][0] is item, arr[n][1] is its priority
        # Accessing obj.arr externally may not lead to the expected results, see _delete
        self.arr = list()
        # Stores indexes of each item for supporting updates and deletion.
        self.pos_map = {}
        # Stores current size of heap.
        self.size = 0
        # Stores function used to evaluate the score of an item on which basis ordering
        # will be done.
        self.key = key or (lambda x: x)

    def _parent(self, i):
        """Returns parent index of given index if exists else None"""
        return int((i - 1) / 2) if i > 0 else None

    def _left(self, i):
        """Returns left-child-index of given index if exists else None"""
        left = int(2 * i + 1)
        return left if 0 < left < self.size else None

    def _right(self, i):
        """Returns right-child-index of given index if exists else None"""
        right = int(2 * i + 2)
        return right if 0 < right < self.size else None

    def _swap(self, i, j):
        """Performs changes required for swapping two elements in the heap"""
        # First update the indexes of the items in index map.
        self.pos_map[self.arr[i][0]], self.pos_map[self.arr[j][0]] = (
            self.pos_map[self.arr[j][0]],
            self.pos_map[self.arr[i][0]],
        )
        # Then swap the items in the list.
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _cmp(self, i, j):
        """Compares the two items using default comparison"""
        return self.arr[i][1] <= self.arr[j][1]

    def _get_valid_parent(self, i):
        """
        Returns index of valid parent as per desired ordering among given index and
        both it's children
        """
        left = self._left(i)
        right = self._right(i)
        valid_parent = i

        if left is not None and not self._cmp(left, valid_parent):
            valid_parent = left
        if right is not None and not self._cmp(right, valid_parent):
            valid_parent = right

        return valid_parent

    def _heapify_up(self, index):
        """Fixes the heap in upward direction of given index"""
        parent = self._parent(index)
        while parent is not None and not self._cmp(index, parent):
            self._swap(index, parent)
            index, parent = parent, self._parent(parent)

    def _heapify_down(self, index):
        """Fixes the heap in downward direction of given index"""
        valid_parent = self._get_valid_parent(index)
        while valid_parent != index:
            self._swap(index, valid_parent)
            index, valid_parent = valid_parent, self._get_valid_parent(valid_parent)

    def update_item(self, item, item_value):
        """Updates given item value in heap if present"""
        if item not in self.pos_map:
            return
        index = self.pos_map[item]
        self.arr[index] = [item, self.key(item_value)]
        # Make sure heap is right in both up and down direction.
        # Ideally only one of them will make any change.
        self._heapify_up(index)
        self._heapify_down(index)

    def delete_item(self, item):
        """Deletes given item from heap if present
        Note: To improve performance we never really delete items from self.arr"""
        try:
            index = self.pos_map[item]
        except:
            raise
        del self.pos_map[item]
        self.arr[index] = self.arr[self.size - 1]
        self.pos_map[self.arr[self.size - 1][0]] = index
        self.size -= 1
        # Make sure heap is right in both up and down direction. Ideally only one
        # of them will make any change- so no performance loss in calling both.
        if self.size > index:
            self._heapify_up(index)
            self._heapify_down(index)

    def insert_item(self, item, priority):
        """Inserts given item with given value in heap"""
        arr_len = len(self.arr)
        if arr_len == self.size:
            self.arr.append([item, self.key(priority)])
        else:
            self.arr[self.size] = [item, self.key(priority)]
        self.pos_map[item] = self.size
        self.size += 1
        self._heapify_up(self.size - 1)

    def heappeek(self):
        """Returns top item tuple (Calculated value, item) from heap if present"""
        return self.arr[0] if self.size else None

    def heappop(self):
        """
        Return top item tuple (Calculated value, item) from heap and removes it as well
        if present
        """
        top_item_tuple = self.heappeek()
        if top_item_tuple:
            self.delete_item(top_item_tuple[0])
        return top_item_tuple


def test_heap() -> None:
    """
    >>> h = Heap()  # Max-heap
    >>> h.insert_item(5, 34)
    >>> h.insert_item(6, 31)
    >>> h.insert_item(7, 37)
    >>> h.heappeek()
    [7, 37]
    >>> h.heappop()
    [7, 37]
    >>> h.heappop()
    [5, 34]
    >>> h.heappop()
    [6, 31]
    >>> h = Heap(key=lambda x: -x)  # Min heap
    >>> h.insert_item(5, 34)
    >>> h.insert_item(6, 31)
    >>> h.insert_item(7, 37)
    >>> h.heappeek()
    [6, -31]
    >>> h.heappop()
    [6, -31]
    >>> h.heappop()
    [5, -34]
    >>> h.heappop()
    [7, -37]
    >>> h.insert_item(8, 45)
    >>> h.insert_item(9, 40)
    >>> h.insert_item(10, 50)
    >>> h.heappeek()
    [9, -40]
    >>> h.update_item(10, 30)
    >>> h.heappeek()
    [10, -30]
    >>> h.delete_item(10)
    >>> h.heappeek()
    [9, -40]
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
