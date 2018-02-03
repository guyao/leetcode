# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if root is None:
                return 0
            else:
                return 1 + depth(root.left)

        def count(root):
            if root is None:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            if left_depth == right_depth:
                return 2 ** left_depth + count(root.right)
            else:
                return 2 ** right_depth + count(root.left)
        return count(root)