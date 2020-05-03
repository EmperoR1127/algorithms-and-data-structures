from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    #----------- nested _Node class -----------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        def __init__(self, element, parent = None, left = None, right = None):
            __slots__ = "_element", "_parent", "_left", "_right"
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            
    #----------- nested Position class -----------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) == type(self) and self._node == other._node

    #----------- nonpublic utilities -----------
    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise ValueError("p must be proper Position type")
        if not (self == p._container):
            raise ValueError("p does not belong to this container")
        if p._node._parent == p._node: # convention for deprecated nodes
            raise ValueError("p is no longer valid")

        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node else None

    #----------- binary tree constructor -----------
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    #----------- public accessors -----------
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._root)

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)"""
        if p == self.root():
            return None
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return a Position representing p's left child
        Return None if p does not have a left child
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return a Position representing p's right child
        Return None if p does not have a right child
        """
        node = self._validate(p)
        return self._make_position(node._right)
        
    def num_children(self, p):
        """Return the number of children that Position p has"""
        node, cnt = self._validate(p), 0
        if node._left:
            cnt += 1
        if node._right:
            cnt += 1
        return cnt

    def add_root(self, e):
        """Place element e at the root of an empty tree and
        return new Position.
        Raise ValueError if tree is not empty
        """
        if not self.is_empty():
            raise ValueError("Tree is not empty")
        self._root = self._Node(e)
        self._size = 1
        return self.root()

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a left child
        """
        if self.left(p):
            raise ValueError("Node has a left child already")
        node = self._validate(p)
        node._left = self._Node(e, node) # set the parent at the same time
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child
        """
        if self.right(p):
            raise ValueError("Node has a right child already")
        node = self._validate(p)
        node._right = self._Node(e, node) # set the parent at the same time
        self._size += 1
        return self._make_position(node._right)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        
        child = node._left if node._left else node._right # child is possibly be None
        if child: # p has a child
            child._parent = node._parent # child's grandparent becomes parent
        if self._root == node: # p is the root
            self._root = child # child now is the root
        else:
            parent = node._parent
            if parent._left == node: # p is its parent's left child
                parent._left = child
            else:
                parent._right = child
            
        node._parent = node # convention for deprecated node
        self._size -= 1
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        if not self.is_leaf(p):
            raise ValueError("p must be a leaf")
        if not (type(self) == type(t1) and type(self) == type(t2)):
            raise TypeError("Tree types must match")
        node = self._validate(p)
        if not t1.is_empty():
            node._left = t1._root
            t1._root._parent = node
            node._size += len(t1)
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            node._right = t2._root
            t2._root._parent = node
            node._size += len(t2)
            t2._root = None
            t2._size = 0

if __name__ == "__main__":
    tree = LinkedBinaryTree()
    tree.add_root(5)
    root = tree.root()
    tree.add_left(root, 4)
    tree.add_right(root, 6)
    print(tree.left(root))
    print(tree.num_children(root))
    print(tree.is_leaf(tree.left(root)))
        
            
    
                    
                
        
        
    
            




















            
