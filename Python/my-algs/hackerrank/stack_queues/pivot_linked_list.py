class Node:
    def __repr__(self):
        node = self
        all_data = []
        while node:
            all_data.append(str(node.data))
            node = node.next
        return ','.join(all_data)



def ll(*args):
    next_node = None
    current = None
    for datum in reversed(args):
        current = Node()
        current.data = datum
        current.next = next_node
        next_node = current
    return current #  head

def find_last(head):
    if not head:
        return None, 0
    size = 1
    while head.next:
        head=head.next
        size += 1
    return head, size
def moveRight(right, prev):
    right.next = prev.next
    prev.next = prev.next.next
    right.next.next = None
    return right.next

def pivot_ll(head, pivot):
    """
    """
    last, length = find_last(head)
    if length <= 1:
        return head

    dummyhead = Node()
    dummyhead.next = head
    dummyhead.data = 'dummy'
    prev = dummyhead
    for _ in range(length - 1):
        #print("begin", locals())
        if prev.next and prev.next.data >= pivot:
            last = moveRight(last, prev) #  moves next node
        else:
            prev = prev.next
        #print('end', locals())

    return dummyhead.next


if __name__=='__main__':

    some_ll = ll(1,0,2,9,3,8,4,7,6,5)
    h = pivot_ll(some_ll, 5)
    print(h)
    some_ll = ll(1,2,3,4,5,6,7,8)
    h = pivot_ll(some_ll, 1)
    print(h)
    some_ll = ll(4,3,2,1)
    h = pivot_ll(some_ll, 2)
    print(h)
    some_ll = ll(1,2,7,8,2,3,9,9)
    h = pivot_ll(some_ll, 5)
    print(h)
    some_ll = ll(3,4,5,1,2,3,6,7,8)
    h = pivot_ll(some_ll, 5)
    print(h)
    some_ll = ll(9,9,9)
    h = pivot_ll(some_ll, 0)
    print(h)
    some_ll = ll()
    h = pivot_ll(some_ll, 5)
    print(h)

