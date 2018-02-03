# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def list_to_int(l):
            res = 0
            for n in l:
                res *= 10
                res += n
            return res

        def dfs(node, path):
            if node is None:
                return
            if node.left is None and node.right is None:
                res.append(list_to_int(path + [node.val]))
                return
            for n in [node.left, node.right]:
                dfs(n, path + [node.val])
        dfs(root, [])
        return sum(res)