class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        dp = [None for _ in range(amount+1)]
        INF = float('inf')
        cs = set(coins)
        def search(n):
            if n < 0:
                return INF
            if dp[n] is not None:
                return dp[n]
            if n in cs:
                dp[n] = 1
                return 1
            result = INF
            for c in coins:
                result = min(search(n - c), result)
            dp[n] = result + 1
            return dp[n]
        search(amount)
        return dp[amount] if dp[amount] != INF else -1

r = Solution().coinChange([1,2,5], 11)
r = Solution().coinChange([2], 1)
r = Solution().coinChange([1], 0)
print(r)
