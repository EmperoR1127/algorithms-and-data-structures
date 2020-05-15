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
            return self._subtree_search(self.left(p), k)
        elif p.key() < k and self.right(p): # k should be in the right subtree of p, if any
            return self._subtree_search(self.right(p), k)
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
        
    def find_position(self, k):
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
            else:
                item = self._Item(k, v)
                print(item._key)
                if p.key() > k:
                    leaf = self.add_left(p, item)
                else:
                    leaf = self.add_right(p, item)
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

    def delete(self, p):
        """Remove the item at given Position"""
        self._validate(p) # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p): # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self.replace(p, replacement.element())
            p = replacement
        parent = self.parent(p) # p has at most one child
        self._delete(p)
        self._rebalance_delete(parent) # if root deleted, parent is None

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        if not self.is_empty():
            p = self._subtree_search(self.root())
            if p.key() == k:
                self.delete(p)
                return
            self._rebalance_access(p) # hook for balanced tree subclasses
        raise KeyError("Invalid k: {}".format(k))

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)"""
        if make_left_child: # make it a left child
            parent._left = child 
        else:   # make it a right child
            parent._right = child 
        if child: # make child point to parent
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent"""
        x = p._node
        y = x._parent # assume y exists
        z = y._parent # z might be None
        if not z: # y is the root
            self._root = x # x becomes the root
            x._parent = None
        else:
            self._relink(z, x, y == z._left) # relink x to be the same child as y to z
        # now rotate x and y, including transfer of middle subtree 
        if y._left == x : # x is the left child of y
            self._relink(y, x._right, True) # relink x_right to be the left child of y
            self._relink(x, y, False) # relink y to be the right child of x
        else:
            self._relink(y, x._left, False) # relink x_left to be the right child of y
            self._relink(x, y, True) # relink y to be the left child of x

    def _restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent"""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.left(y) and y == self.left(z)) or (x == self.right(y) and y == self.right(z)): # single rotation
            self._rotate(y)
            return y # y is new subtree root
        else: # double rotation
            self._rotate(x)
            self._rotate(x)
            return x # x is new subtree root
        
    def _rebalance_access(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_insert(self, p):
        pass
    
    def _rebalance_access(self, p):
        pass
    

if __name__ == "__main__":
    tree = TreeMap()
    tree[5] = "sdasd"
    tree[5] = "dfdg"
    tree[6] = "hk"
    #print(tree[5])
    
        
        
            
    











    
            
        
            
