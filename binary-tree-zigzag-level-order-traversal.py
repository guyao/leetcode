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
root = deserialize([1,2,3,4,None,None,5])

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = [root]
        res = []
        r = False
        while q:
            nxt = []
            level = []
            if r:
                level = [node.val for node in q[::-1]]
                r = False
            else:
                level = [node.val for node in q]
                r = True
            for node in q:
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            res.append(level[:])
            q = nxt
        return res

Solution().zigzagLevelOrder(root)
        