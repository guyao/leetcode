"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INF = float('inf')
        d = [0] + [i-j for i, j in zip(prices[1:], prices[:-1])]
        hold1 = -INF
        release1 = 0
        hold2 = -INF
        release2 = 0
        for price in prices:
            release2 = max(release2, hold2 + price) #sold 2nd
            hold2 = max(hold2, release1 - price) #buy 2nd
            release1 = max(release1, hold1 + price) #sold 1st
            hold1 = max(hold1, -price) #buy 1st
        return release2

"""
before[i] max sum before i
after[i] max sum after i
"""


class Solution(object):
    def maxProfit(self, prices):
        before = [0 for i in range(len(prices))] #[0, i]
        after = [0 for i in range(len(prices))] #[i, ed]
        diff = [0] + [i-j for i, j in zip(prices[1:], prices[:-1])]
        max_ending_here = 0
        max_so_far = 0
        for i in range(len(prices)):
            max_ending_here = max(0, max_ending_here + diff[i])
            max_so_far = max(max_so_far, max_ending_here)
            before[i] = max_so_far

        diff = [i-j for i, j in zip(prices[1:], prices[:-1])] + [0]
        max_start_here = 0
        max_so_far = 0
        for i in reversed(range(len(prices))):
            max_start_here = max(0, max_start_here + diff[i])
            max_so_far = max(max_so_far, max_start_here)
            after[i] = max_so_far

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, before[i] + after[i])
        return max_profit


t = [7, 1, 4, 3, 5, 14, 0, 8, 4, 2, 4, 5, 1, 9, 4]
t = [3,2,6,5,0,3] #expect 7
print()
r = Solution().maxProfit(t)