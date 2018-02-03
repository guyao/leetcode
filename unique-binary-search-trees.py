class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {}
        def dfs(nums):
            if not nums:
                return 1
            if memory.get(tuple(nums)):
                return memory.get(tuple(nums))
            res = []
            for i in range(len(nums)):
                a = nums[:i]
                b = nums[i+1:]
                res.append(dfs(a) * dfs(b))
            res = sum(res)
            memory[tuple(nums)] = res
            return res
        return dfs(list(range(1, n + 1)))

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n + 1):
            res = 0
            for j in range(i):
                res += dp[j] * dp[i - j - 1]
            dp[i] = res
        return dp[-1]