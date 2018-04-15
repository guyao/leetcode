# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        s = []
        for n in nums:
            node = TreeNode(n)
            while s and s[-1].val < node.val:
                node.left = s[-1]
                s.pop()
            if s:
                s[-1].right = node
            s.append(node)
        return s[0] if s else None