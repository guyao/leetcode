# backtracking 
"""
row = r 
col = c
(r, c) have two choices: right or bottom
"""
# exceed time limit
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.backtrack(0, 0, m, n)

    def backtrack(self, r, c, m, n):
        if r == m - 1 and c == n - 1:
            return 1
        if r >= m or c >= n:
            return 0
        return self.backtrack(r + 1, c, m, n) + self.backtrack(r, c + 1, m, n)

# Backtracking using memoization:
# Top Down DP
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.dp = [[None for _ in range(n + 1)] for i in range(m + 1)]
        return self.backtrack(0, 0, m, n)


    def backtrack(self, r, c, m, n):
        if r == m - 1 and c == n - 1:
            return 1
        if r >= m or c >= n:
            return 0
        if self.dp[r + 1][c] is None:
            self.dp[r + 1][c] = self.backtrack(r + 1, c, m, n)
        if self.dp[r][c + 1] is  None:
            self.dp[r][c + 1] = self.backtrack(r, c + 1, m, n)
        return self.dp[r + 1][c] + self.dp[r][c + 1]

# Bottom up DP
"""

We observe that all grids of the bottom edge and right edge must all have only
one unique path to the bottom-right corner. Using this as the base case, we
can build our way up to our solution at grid (1, 1) using the relationship
above.

s   21  15  10  6   3   1
7   6   5   4   3   2   1   
1   1   1   1   1   1   end

"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 if (i == m - 1) or (j == n - 1) else None for j in range(n)] for i in range(m)]
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[m-1][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

# Combinatorial Solution
# Solution of m*n is C(m+n-2)(m-1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = 1
        for i in range(m-1):
            ret *= (m + n - 2 - i)
        for i in range(m-1):
            ret /= (i + 1)
        return ret

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from functools import reduce
        n = m + n - 2
        r = m - 1
        return reduce(lambda x, y: x * y[0] / y[1], zip(range(n - r + 1, n+1), range(1, r+1)), 1)


r = Solution().uniquePaths(3, 7)