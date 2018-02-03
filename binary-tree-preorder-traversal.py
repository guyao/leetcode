# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root):
            if root is None:
                return []
            return [root.val] + traverse(root.left) + traverse(root.right)
        return traverse(root)
