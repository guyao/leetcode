# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(lst):
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

root = deserialize([3, 9, 20, None, None, 15, 7])

class Solution(object):
    def levelOrderBottom(self, root):
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
        return list(reversed(res))
        