"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inc = [i - j if i > j else 0 for i, j in zip(prices[1:], prices[:-1])]
        return sum(inc)


t = [7, 1, 4, 3, 5]
r = Solution().maxProfit(t)
