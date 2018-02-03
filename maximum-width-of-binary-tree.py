# https://leetcode.com/problems/maximum-width-of-binary-tree

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        INF = float('inf')

        q = [root]
        res = -INF

        while q:
            level = []
            res = max(len(q), res)
            for i in range(len(q)):
                node = q[i]

                if node is not None:
                    level.append(node.left)
                    level.append(node.right)
                elif node is None:
                    level.append(None)
                    level.append(None)

            l = 0
            while l < len(level) and level[l] is None:
                l += 1

            r = len(level) - 1
            while l <= r and level[r] is None:
                r -= 1

            q = level[l: r + 1]
        return res