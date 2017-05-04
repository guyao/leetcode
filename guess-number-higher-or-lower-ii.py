"""
if the feedback is always bad and therefore leads to wrose branch

best way to search:
each range [lo, hi]
for i in [lo, hi], goto i
which cost less
Search all possible range at last

DP:
    result when pick x = x + max(
        dp(i - x-1),
        dp(x+1, j)
    )
"""
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        INF = float('inf')
        dp = [[None]*(n+1) for _ in range(n+1)]
        def helper(lo, hi):
            if lo >= hi:
                if dp[hi][hi] is None:
                    dp[hi][hi] = 0
                return 0
            if dp[lo][hi] is not None:
                return dp[lo][hi]
            candidate = INF
            for i in range(lo, hi+1):
                cost = i + max(
                    helper(lo, i-1),
                    helper(i+1, hi)
                    )
                candidate = min(candidate, cost)
            dp[lo][hi] = candidate
            return candidate
        helper(1, n)
        return dp[1][n]

r = Solution().getMoneyAmount(1)
print(r)