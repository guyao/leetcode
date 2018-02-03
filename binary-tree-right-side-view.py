# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        q = [root]
        while q:
            level = []
            res.append(q[-1].val)
            for node in q:
                for n in [node.left, node.right]:
                    if n is not None:
                        level.append(n)
            q = level
        return res