# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_symmetric(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)
        return root is None or is_symmetric(root.left, root.right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q:
            level = []
            l = 0
            r = len(q) - 1
            while l < r:
                if ((q[l] is None) and (q[r] is None)) or (((q[l] is not None) and (q[r] is not None)) and (q[l].val == q[r].val)):
                    l += 1
                    r -= 1
                else:
                    return False

            for node in q:
                if node is not None:
                    for n in [node.left, node.right]:
                        level.append(n)
            q = level
        return True