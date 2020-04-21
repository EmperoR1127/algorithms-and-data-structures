class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    #------------------------------- nested Node class----------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        def __init__(self, element, prev = None, next = None):
            __slots__ = "_element", "_prev", "_next"
            self._element = element
            self._prev = prev
            self._next = next

        def __str__(self):
            return str(self._element)
        
    #------------------------------- list methods -------------------------

    def __init__(self):
        self._header = self._Node(None)
        self._tailer = self._Node(None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
        if predecessor._next != successor and successor._prev != predecessor:
            raise ValueError("predecessor and successor aren't adjacent")
        node = self._Node(e, predecessor, successor)
        predecessor._next, successor._prev = node, node # update the link of neighbors
        self._size += 1
        return node
        

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        prev, next, element = node._prev, node._next, node._element # find the neighbors
        prev._next, next._prev = next, prev
        node._prev = node._next = node._element = None # depricate node
        self._size -= 1
        return element











    

























    
        
    
