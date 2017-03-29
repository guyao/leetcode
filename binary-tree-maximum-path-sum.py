# Binary Tree Maximum Path Sum

"""
Try the bottom up approach. At each node,
the potential maximum path could be one of these cases:

i. max(left subtree) + node
ii. max(right subtree) + node
iii. max(left subtree) + max(right subtree) + node
iv. the node itself
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum = -float('inf')
        self.findMax(root)
        return self.maxsum

    def findMax(self, node):
        if node is None:
            return 0
        left = self.findMax(node.left)
        right = self.findMax(node.right)
        self.maxsum = max(left+node.val, right+node.val, left+right+node.val, node.val, self.maxsum)
        ret = max(left+node.val, right+node.val, node.val)
        return ret