from DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""
    #------------------------- nested Position class----------------------
    class Position:
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._tailer:
            return None
        return self.Position(self, node)

    def first(self):
        """Return the position of the first element of L, or None if L is empty."""
        if self.is_empty():
            return None
        return self._make_position(self._header._next)

    def last(self):
        """Return the position of the last element of L, or None if L is empty"""
        if self.is_empty():
            return None
        return self._make_position(self._tailer._prev)

    def before(self, p):
        """Return the position of L immediately before position p,
        or None
        if p is the first position
        """
        node = self._validate(p)
        if node._prev == self._header: # the first node
            return None
        return self._make_position(node._prev)

    def after(self, p):
        """Return the position of L immediately after position p,
        or None if 
        p is the last position.
        """
        node = self._validate(p)
        if node._next == self._tailer: # the last node
            return None
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor != None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list"""
        cursor = self.last()
        while cursor != None:
            yield cursor.element()
            cursor = self.before(cursor)

    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert a new element e at the front of L,
        returning the position
        of the new element.
        """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert a new element e at the back of L,
        returning the position of the new element
        """
        return self._insert_between(e, self._tailer._prev, self._tailer)

    def add_before(self, e, p):
        """Insert a new element e just before position p in L,
        returning the position of the new element.
        """
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, e, p):
        """Insert a new element e just after position p in L,
        returning the position of the new element.
        """
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def replace(self, p, e):
        """Replace the element at position p with element e,
        returning the element formerly at position p.
        """
        node = self._validate(p)
        res, node._element = node._element, e
        return res

    def delete(self, p):
        """Remove and return the element at position p in L,
        invalidating the position.
        """
        node = self._validate(p) # retrieve the node about to delete
        return self._delete_node(node)

    def max(self):
        """returns the maximum element from a PositionalList"""
        value = self.first().element()
        for walk in iter(self):
            if value < walk:
                value = walk
        return value

    def find(self, e):
        """Return the position of the first appearance of element e in the list
        None if not found
        """
        walk = self.first()
        while walk != None:
            if walk.element() == e: # find e
                return walk
        return None

 
def insertion_sort(pl):
    """Sort PositionalList of comparable elements into non decreasing order"""
    if not isinstance(pl, PositionalList):
        raise ValueError("Wrong type")
    if len(pl) <= 1: # no need to sort
        return pl

    marker = pl.first()
    # all the postions before maker have been sorted
    while marker != pl.last():
        pivot = pl.after(marker) # the position about to sort
        value = pivot.element()
        
        if marker.element() > value: # need to insert
            walk = marker
            while walk != pl.first() and pl.before(walk).element() > value:
                walk = pl.before(walk)
            # insert pivot into the right position
            pl.add_before(value, walk)
            pl.delete(pivot)
        else:
            # the pivot is already sorted
            # just move marker to the right
            marker = pivot

def bubble_sort(pl):
    """Sort PositionalList of comparable elements into non decreasing order"""
    if not isinstance(pl, PositionalList):
        raise ValueError("Wrong type")
    if len(pl) <= 1: # no need to sort
        return pl

    end = pl.last()
    for i in range(1, len(pl)):
        walk = pl.first()
        while walk != end:
            next = pl.after(walk)
            if next.element() < walk.element(): # swap the elements
                temp = walk.element()
                pl.replace(walk, next.element())
                pl.replace(next, temp)
            walk = next
        end = pl.before(end)

def pairOfPositions(pl, value):
    """Check if the sum of two elments in different positions in a
    sorted positional list equals value
    None otherwise
    """
    if len(pl) < 2:
        return None
    insertion_sort(pl)
    lo, hi = pl.first(), pl.last()
    while lo != hi:
        if lo.element() + hi.element() < value:
            lo = pl.after(lo)
        elif lo.element() + hi.element() > value:
            hi = pl.before(hi)
        else:
            return lo, hi
    return None


if __name__ == "__main__":
    pl = PositionalList()
    pl.add_first(5)
    pl.add_last(4)
    pl.add_last(6)
    pl.add_last(10)
    pl.add_last(8)
    pl.add_last(1)
    pl.add_last(2)
    pl.add_last(1)
    bubble_sort(pl)
    for p in iter(pl):
        print(p)
    print("--------")
    for p in reversed(pl):
        print(p)
