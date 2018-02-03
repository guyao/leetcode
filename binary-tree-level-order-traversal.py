# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = [root]
        res = []
        while q:
            nxt = []
            level = []
            for node in q:
                level.append(node.val)
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            q = nxt
            res.append(level[:])
        return res