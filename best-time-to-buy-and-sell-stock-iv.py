"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        if k >= len(prices) // 2:
            diff = [i-j if i-j > 0 else 0 for i,j in zip(prices[1:], prices[:-1])]
            return sum(diff)
        diff = [0] + [i-j for i,j in zip(prices[1:], prices[:-1])]
        dp = [[0 for _ in range(len(prices)) ] for _ in range(k+1)]
        for i in range(1, k+1):
            tmp_max = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(
                    prices[j] + tmp_max,
                    dp[i][j-1]
                    )
                tmp_max = max(
                    tmp_max,
                    dp[i-1][j-1] - prices[j]
                    )
        return dp[k][-1]

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        if k >= len(prices) // 2:
            diff = [i-j if i-j > 0 else 0 for i,j in zip(prices[1:], prices[:-1])]
            return sum(diff)
        diff = [0] + [i-j for i,j in zip(prices[1:], prices[:-1])]
        dp = [[0 for _ in range(len(prices)) ] for _ in range(k+1)]
        for i in range(1, k+1):
            max_ending_here = 0
            max_so_far = 0
            for j in range(1, len(prices)):
                max_ending_here = max(dp[i-1][j-1] + max(0, diff[j]), max_ending_here + diff[j])
                max_so_far = max(max_so_far, max_ending_here)
                dp[i][j] = max(
                    max_so_far,
                    dp[i-1][j]
                    )

        return dp[k][-1]

# t = (4, [5,8,2,3,7,4,6,7,9,1,2,7,5,6,7,3,4,2,8,7,5,4,1,2,5,6,3,4,5,9,7,2,3,5,6,7,8,2,5])
t = (2, [3,2,6,5,0,3])
print()
r = Solution().maxProfit(*t) #expect 28