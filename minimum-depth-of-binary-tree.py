# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        INF = float('inf')

        def helper(root):
            if root is None:
                return 0
            l = helper(root.left)
            l = l if l != 0 else INF
            r = helper(root.right)
            r = r if r != 0 else INF
            m = min(l, r)
            return m + 1 if m != INF else 1

        return helper(root)

