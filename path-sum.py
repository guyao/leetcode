# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(root, v):
            if root.left is None and root.right is None:
                if root.val == v:
                    return True
            for n in root.left, root.right:
                if n is not None:
                    if dfs(n, v - root.val):
                        return True
            return False

        if root is None:
            return False

        return dfs(root, sum)