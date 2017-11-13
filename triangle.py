# Triangle
# https://leetcode.com/problems/triangle/description/


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[item for item in range(len(l))] for l in triangle]
        dp.append([0] * (len(triangle[-1]) + 1))
        for i in reversed(range(len(triangle))):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]
