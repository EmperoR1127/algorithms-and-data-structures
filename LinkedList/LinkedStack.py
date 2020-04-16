class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    
    #-------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        def __init__(self, element, next = None):
            __slots__ = "_element", "_next"
        
            self._element = element
            self._next = next

    #------------------------------- stack methods -------------------------

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        #Create and link a new node
        #assign head to the new node
        self._head = self._Node(value, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Empty stack")
        node = self._head
        #link head to the next node
        self._head = self._head._next
        self._size -= 1
        return node._element

    def top(self):
        if self.is_empty():
            raise ValueError("Empty stack")

        return self._head._element


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(3)
    stack.push(4)
    stack.push("s")
    while len(stack) != 0:
        print(stack.pop())


























        

    
