# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def output(l):
            return "->".join([str(i) for i in l])

        paths = []

        if not root:
            return paths

        def dfs(root, path):
            if (root.left is None) and (root.right is None):
                paths.append(path + [root.val])
                return
            if root.left is not None:
                dfs(root.left, path + [root.val])
            if root.right is not None:
                dfs(root.right, path + [root.val])

        dfs(root, [])
        return [output(p) for p in paths]