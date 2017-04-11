"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
"""
Stack

Loop Invariant:
    current: smallest
    next: smallest of right node
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_stack(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            node = self.stack.pop()
            self.push_stack(node.right)
            return node.val


    def push_stack(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
"""
Generator:
    Inorder Traversal
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def traverse(node):
            if node is None:
                return
            for i in traverse(node.left):
                yield i
            yield node.val
            for i in traverse(node.right):
                yield i
        self.iter = traverse(root)
        self.q = []
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.q:
            try:
                v = next(self.iter)
                self.q.append(v)
            except StopIteration:
                return False
        return True
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            v = self.q.pop()
            return v
        


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

#Test
def deserialize(lst):
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

t = [6, 3, 7, None, 4, None, None, None, 5]
t = deserialize(t)
r = BSTIterator(t)
