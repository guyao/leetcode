"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        length = len(prices)
        buy = [0 for _ in range(length)]
        sell = [0 for _ in range(length)]
        rest = [0 for _ in range(length)]
        buy[0] = -prices[0]
        for i in range(1, length):
            price = prices[i]
            buy[i] = max(rest[i-1]-price, buy[i-1])
            sell[i] = max(buy[i-1]+price, sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        return sell[-1]

# A further observation:
# rest[i] <=sell[i]
# substitute buy[i]
"""
buy[i] = max(sell[i-2]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell

# State Machine
"""
s0 buy -> s1
s0 rest -> s0
s1 sell -> s2
s1 rest -> s1
s2 rest -> s0
"""

"""
s0[i] stay at s0 or rest from s2
s0[i] = max(s0[i-1], s2[i-1])

s1[i] stay at s1, or buy from s0
s1[i] = max(s1[i-1], s0[i-1]-prices[i])

s2[i] only one way from s1
s2[i] = s1[i-1] + prices[i]

define base case:
s0[0] = 0
s1[0] = -prices[0] (after buy, should have -prices[0])
s2[0] = INT_MIN (lower base case)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INF = float('inf')
        length = len(prices)
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [-INF]
        for i in range(1, length):
            s0.append(
                max(s0[i-1], s2[i-1])
                )
            s1.append(
                max(s1[i-1], s0[i-1]-prices[i])
                )
            s2.append(
                max([s1[i-1]+prices[i]])
                )
        return max(
            s0[length - 1],
            s2[length - 1]
            )

"""
buy[i] = max(buy[i-1], sell[i-2] - prices[i])
sell[i] = max(sell[i-1], buy[i-1] + prices[i])

b0 = max(b1, s2-price)
s0 = max(s1, b1+price)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        b0 = -prices[0]
        b1 = -prices[0]
        s0 = 0
        s1 = 0
        s2 = 0
        for price in prices[1:]:
            b0 = max(b1, s2 - price)
            s0 = max(s1, b1 + price)
            b1 = b0
            s2 = s1
            s1 = s0
        return s0

t = [1, 2, 3, 0, 2]
t = [1, 2, 3, 0, 2, 5,9,2,4,1,7,3,5]
r = Solution().maxProfit(t)

