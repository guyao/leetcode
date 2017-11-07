# https://leetcode.com/problems/longest-univalue-path/
"""
depth = max(children's depth) + 1
length = sum of max 2 children + 1
"""
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = {}
        d = {}
        from collections import defaultdict
        l = defaultdict(int)
        d[None] = 0
        def dfs(node, v):
            if node is None:
                return 0
            if node.val != v:
                d[node] = (dfs(node, node.val))
                return 0
            d[node] = max(dfs(node.left, v), dfs(node.right, v)) + 1
            v1 = 0
            if node.left is not None and node.left.val == v:
                v1 = d[node.left]
            v2 = 0
            if node.right is not None and node.right.val == v:
                v2 = d[node.right]
            l[v] = max(v1 + v2 + 1, l[v])
            return d[node]
        dfs(root, root.val)
        return max([l[k] for k in l]) - 1