from LinkedBinaryTree import LinkedBinaryTree
from MapBase import Mapbase

class TreeMap(LinkedBinaryTree, Mapbase):
    """Sorted map implementation using a binary search tree"""
    #---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map s key-value pair"""
            return self.element()._key

        def value(self):
            """Return value of map s key-value pair"""
            return self.element()._value

    #------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        """Return Position of p s subtree having key k, or last node searched"""
        if p.key() == k:
            return p
        elif p.key() > k and self.left(p): # k should be in the left subtree of p, if any
            self._subtree_search(self.left(p), k)
        elif p.key() < k and self.right(p): # k should be in the right subtree of p, if any
            self._subtree_search(self.right(p), k)
        else:
            return p # unsucessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk): 
            walk = self.left(walk) # keep walking left
        return p

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p"""
        walk = p
        while self.right(walk):
            walk = self.right(walk) # keep walking right
        return walk

    #------------------------------- public methods -------------------------------
    def first(self):
        """Return the first Position in the tree (or None if empty)"""
        if self.is_empty():
            return None
        return self._subtree_first_position(self.root())

    def last(self):
        """Return the last Position in the tree (or None if empty)"""
        if self.is_empty():
            return None
        return self._subtree_last_position(self.root())

    def before(self, p):
        """Return the Position just before p in the natural order
        Return None if p is the first position
        """
        self._validate(p)
        left = self.left(p)
        if left: # p has a left child
            # the position before p will be the last position in its left subtree
            return self._subtree_last_position(left)
        else: # p doesn't have a left child
            walk, p = p, self.parent(p)
            while p and self.left(p) == walk:
                walk, p = p, self.parent(p) # until find walk is the right child of parent
            return p

    def after(self, p):
        """Return the Position just after p in the natural order
        Return None if p is the last position
        """
        self._validate(p)
        right = self.right(p)
        if right: # p has a right child
            # the position after p will be the first position in its right subtree
            return self._subtree_first_position(right)
        else: # p doesn't have a right chid
            walk, p = p, self.parent(p)
            while p and self.right(p) == walk:
                walk, p = p, self.parent(p) # until find walk is the left child of parent
            return p

    def find_position(self, k)
        """Return position with key k, or else neighbor (or None if empty)"""
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p) # hook for balanced tree subclasses
        return p

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)"""
        if self.is_empty():
            return None
        p = self.first()
        return p.key(), p.value()

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k
        Return None if there does not exist such a key
        """
        p = self.find_position(k)
        if p.key() < k:
            p = self.after(p)
        return p.key(), p.value() if p else None

    def find_range(self, start = None, stop = None):
        """Iterate all (key,value) pairs such that start <= key < stop
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        start_p = None
        if not start:
            start_p = self.first()
        else:
            start_p = self.self.find_position(start)
            if start_p and start_p.key() < start:
                start_p = self.after(start_p)
        while start_p and (not stop or start_p.key() < stop):
            yield start_p.key(), start_p.value()
            start_p = self.after(start_p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        if self.is_empty():
            raise KeyError("Invalid k: {}".format(k))
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p) # hook for balanced tree subclasses
        if p.key() != k:
            raise KeyError("Invalid k: {}".format(k))
        return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        if self.is_empty():
            leaf = self.add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p) # hook for balanced tree subclasses
                return
            elif p.key() > k:
                leaf = self.add_left(p, self._Item(k, v))
            else:
                leaf = self.add_right(p, self._Item(k, v))
        self._rebalance_insert(leaf) # hook for balanced tree subclasses

    def __iter__(self):
        """Generate an iteration of all keys in the map in order"""
        walk = self.first()
        while walk:
            yield walk.key()
            walk = self.after(walk)
        
        
            
    def _rebalance_access(self, p):
        pass












    
            
        
            
