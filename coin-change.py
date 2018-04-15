# Time Limit Exceed
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = float('inf')
        dp = [[INF] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] <= j:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1] != INF else -1

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = float('inf')
        dp = [INF for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return dp[-1] if dp[-1] != INF else -1

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
