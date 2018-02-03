# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def is_same(r1, r2):
            if r1 is None or r2 is None:
                return r1 == r2
            if r1.val != r2.val:
                return False
            else:
                return is_same(r1.left, r2.left) and is_same(r1.right, r2.right)
        return is_same(p, q)