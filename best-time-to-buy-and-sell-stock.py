"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        min_price = prices[0]
        for price in prices:
            if price > min_price:
                profit = max(profit, price - min_price)
            else:
                min_price = price
        return profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inc = [0] + [i-j for i,j in zip(prices[1:], prices[:-1])]
        here = 0
        so_far = 0
        for i in inc:
            here = max(0, here + i)
            so_far = max(so_far, here)
        return so_far


            



t = [7, 1, 5, 3, 6, 4]
# t = [7, 6, 4, 3, 1]
r = Solution().maxProfit(t)
