# BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def squares(n):
            s = 1
            squares = []
            while s * s <= n:
                squares.append(s*s)
                s += 1
            return squares

        q = [n]
        depth = 0
        while q:
            nxt = []
            for n in q:
                for candidate in squares(n):
                    if n - candidate == 0:
                        return depth + 1
                    if n - candidate > 0:
                        nxt.append(n - candidate)
            q = nxt
            depth += 1

# DP
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        INF = float('inf')
        dp = [INF for _ in range(n + 1)]
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1

        for i in range(n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]