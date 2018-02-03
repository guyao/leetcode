# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root):
            if root is None:
                return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1
        return max_depth(root)