# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INF = float('inf')

        def depth(root):
            if root is None:
                return 0
            dl = depth(root.left)
            dr = depth(root.right)


            if abs(dl - dr) > 1:
                return INF
            return max(dl, dr) + 1
        return False if depth(root) == INF else True