from DoublyLinkedBase import _DoublyLinkedBase

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list"""

    # ---------- nonpublic utilities ----------
    def __iter__(self):
        cursor = self._header._next
        while cursor != self._tailer:
            yield cursor._element
            cursor = cursor._next

    # ---------- public methods ----------

    def first(self):
        if self.is_empty():
            raise ValueError("Empty deque")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError("Empty deque")
        return self._tailer._prev._element

    def insert_first(self, e):
        # insert after header
        return self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        # insert before tailer
        return self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Empty deque")
        # delete the node after header
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Empty deque")
        # deleter the node before tailer
        return self._delete_node(self._tailer._prev)


if __name__ == "__main__":
    dq = LinkedDeque()
    dq.insert_first(5)
    dq.insert_last(4)
    dq.insert_last(3)
    dq.insert_last(1)
    dq.insert_last(9)

    for e in iter(dq):
        print(e)






    
