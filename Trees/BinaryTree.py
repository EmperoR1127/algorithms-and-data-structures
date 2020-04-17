from Tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""
    
    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p s sibling (or None if no sibling)"""
        parent = self.parent(p) # find the parent Position
        if not parent: # p is the root Position
            return None
        if p == self.left(parent): # p is the left child of parent Position
            return self.right(parent)
        else: # p is the right child of parent Position
            return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)






















            
        
