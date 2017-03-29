"""
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0:
            return 0
        # dp = [[ 1 if ((i == m-1) or (j == n -1)) and (obstacleGrid[i][j] != 1) \
        #     else (0 if obstacleGrid[i][j] == 1 else None) \
        #     for j in range(n)] \
        #     for i in range(m)]
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[m-1][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] if obstacleGrid[i][j] != 1 else 0
        for d in dp:
            print(d)
        return dp[0][0]

r = Solution().uniquePathsWithObstacles(t)