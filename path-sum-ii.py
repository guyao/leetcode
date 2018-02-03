class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root, path, target):
            if root is None:
                return
            if (root.left is None) and (root.right is None):
                if root.val != target:
                    return
                result = path + [root.val]
                res.append(result[:])
                return
            dfs(root.left, path + [root.val], target - root.val)
            dfs(root.right, path + [root.val], target - root.val)
        dfs(root, [], sum)
        return res