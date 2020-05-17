class LinkedQueue():
    """FIFO queue implementation using a singly linked list for storage."""

    #------------------------------- nested Node class---------------------- 
    class _Node():
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next = None):
            __slots__ = "_element", "_next"
            self._element = element
            self._next = next

    #------------------------------- queue methods -------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        node = self._Node(value)
        if self.is_empty(): # enqueue the first node
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        node = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # the queue is empty after dequeue
            self._tail = None # update the tail
        
        return node._element

    def front(self):
        if self.is_empty():
            raise ValueError("Empty queue")
        return self._head._element
        
def reverse(node):
    """Reverse the list after the given node"""
    if node._next == None:
        return node
    new_head = reverse(node._next)
    node._next._next = node
    node._next = None
    return new_head

def non_recursive_reverse(node):
    """Reverse the list after the given node, non-recursively"""
    prev, curr = None, node
    while curr != None:
        next = curr._next
        curr._next = prev # point to the previous node
        prev = curr
        curr = next
    return prev


if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue("s")
    q.enqueue(9)
    q.enqueue(10)
    l = non_recursive_reverse(q._head)
    while l != None:
        print(l._element)
        l = l._next
        























            
