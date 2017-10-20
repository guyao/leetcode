"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        X = "1"
        INF = float('inf')
        m = len(matrix)
        n = len(matrix[0]) if len(matrix) > 0 else 0
        h = [0 for _ in range(n)]
        l = [-INF for _ in range(n)]
        r = [INF for _ in range(n)]
        max_area = 0
        for i in range(m):
            cur_l = 0
            cur_r = n
            for j in range(n):
                if matrix[i][j] == X:
                    h[j] = h[j] + 1
                else:
                    h[j] = 0
            for j in range(n):
                if matrix[i][j] == X:
                    l[j] = max(l[j], cur_l)
                else:
                    l[j] = -INF
                    cur_l = j + 1
            for j in reversed(range(n)):
                if matrix[i][j] == X:
                    r[j] = min(r[j], cur_r)
                else:
                    r[j] = INF
                    cur_r = j
            for j in range(n):
                d = r[j] - l[j]
                area = min(d, h[j]) ** 2
                if d != INF:
                    max_area = max(max_area, area)
        return max_area

"""
State: 
    f[i][j] = max side length of a square that lower right (i,j)
function:
  if matrix i,j == 1
    f(i,j) = min(f(i-1,j-1), f(i,j-1), f(i-1,j)) + 1
  else
    f(i,j) = 0
Intialization
  f(i,0) = matrix(i,0)
  f(0,j) = matrix(0,j)
Answer
  max(f(i,j))
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if len(matrix) > 0 else 0
        dp = [[0 for j in range(n)] for i in range(m)]
        max_side = 0
        for i in range(n):
            dp[0][i] = 1 if matrix[0][i] == "1" else 0
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            if any(dp[i]):
                max_side = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2

t = ["10100","10111","11111","10010"]
r = Solution().maximalSquare(t)