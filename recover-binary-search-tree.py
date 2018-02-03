# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        INF = float('inf')
        self.pre_element = TreeNode(-INF)
        self.first_element = None
        self.second_element = None
        self.preval = -INF
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            if not self.first_element and self.pre_element.val > root.val:
                self.first_element = self.pre_element
            if self.first_element and self.pre_element.val > root.val:
                self.second_element = root
            self.pre_element = root
            traverse(root.right)
        traverse(root)
        self.first_element.val, self.second_element.val = self.second_element.val, self.first_element.val
