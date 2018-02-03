# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(root):
            if root is not None:
                for val in traverse(root.left):
                    yield val
                yield root.val
                for val in traverse(root.right):
                    yield val
        for val in traverse(root):
            if k == 1:
                return val
            else:
                k -= 1