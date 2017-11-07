# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = -float('inf')

        def valid(root):
            self.pre
            if root is None:
                return True
            if not valid(root.left):
                return False
            if self.pre >= root.val:
                return False
            self.pre = root.val
            if not valid(root.right):
                return False
            return True
        return valid(root)
