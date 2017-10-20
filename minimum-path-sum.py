class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                        continue
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = list(grid[0])
        for j in range(1, len(grid[0])):
            s[j] = s[j-1] + grid[0][j]
        for i in range(1, len(grid)):
            s[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                s[j] = min(s[j], s[j-1]) + grid[i][j]
        return s[-1]