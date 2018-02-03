# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(lst):
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

root = deserialize([1, 2, 5, 3, 4, None, 6])

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def traverse(root):
            if root is None:
                return None
            temp = root.right
            traverse(root.left)
            traverse(root.right)
            root.right = root.left
            root.left = None
            while root.right is not None:
                root = root.right
            root.right = temp
        traverse(root)

Solution().flatten(root)
while root is not None:
    print(root.val)
    root = root.right