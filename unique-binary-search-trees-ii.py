class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def cp(t):
            if t is None:
                return None
            root = TreeNode(t.val)
            root.left = cp(t.left)
            root.right = cp(t.right)
            return root

        def dfs(nums):
            if not nums:
                return [None]
            res = []
            for i in range(len(nums)):
                left = dfs(nums[:i])
                right = dfs(nums[i+1:])

                for l in left:
                    for r in right:
                        root = TreeNode(nums[i])
                        root.left = cp(l)
                        root.right = cp(r)
                        res.append(root)
            return res
        return dfs(list(range(1, n + 1)))