"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
"""

class Solution(object):
    def maximalRectangle(self, matrix):
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
                if d != INF:
                    max_area = max(max_area, d*h[j])
        return max_area



        
t = ["10100","10111","11111","10010"]
t = []
r = Solution().maximalRectangle(t)
