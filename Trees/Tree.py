class Tree:
    """Abstract base class representing a tree structure"""
    #----------------- nested Position class -----------------
    class Position:
        """An abstraction representing the location of a single element"""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other Position does not represent the same location"""
            return not (self == other) # opposite as __eq__

        # ---------- abstract methods that concrete subclass must support ----------
        def root(self):
            """Return Position representing the tree s root (or None if empty)"""
            raise NotImplementedError("must be implemented by subclass")

        def parent(self, p):
            """Return Position representing p s parent (or None if p is root)."""
            raise NotImplementedError("must be implemented by subclass")

        def num_children(self, p):
            """Return the number of children that Position p has"""
            raise NotImplementedError("must be implemented by subclass")

        def children(self, p):
            """Generate an iteration of Positions representing p s children"""
            raise NotImplementedError("must be implemented by subclass")

        def __len__(self):
            """Return the total number of elements in the tree"""
            raise NotImplementedError("must be implemented by subclass")

        # ---------- concrete methods implemented in this class ----------
        def is_root(self, p):
            """Return True if Position p represents the root of the tree."""
            return p == self.root()

        def is_leaf(self, p):
            """Return True if Position p does not have any children"""
            return self.num_children(p) == 0

        def is_empty(self):
            """Return True if the tree is empty"""
            return len(self) == 0

        def depth(self, p):
            """Return the number of levels separating Position p from the root."""
            if self.is_root(p): # the depth of root is 0
                return 0
            # if p is not root, then the depth of p is
            # the depth of its parent plus 1
            return self.depth(self.parent(p)) + 1

        def height(self, p = None):
            """Return the height of the subtree rooted at Position p
            If p is None, return the height of the entire tree.
            """
            if not p:
                p = self.root()
            return self._height(p)

        def _height(self, p):
            """Return the height of the subtree rooted at Position p"""
            if self.is_leaf(p): # the height of leaf is 0
                return 0
            # if p is not leaf, then the height of p is
            # the maximum height of its children plus 1
            return max(self._height(child) for child in self.children(p)) + 1


















        
