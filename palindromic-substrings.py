class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        def helper(l, r):
            nonlocal count
            while l <= r and l >= 0 and r <= n - 1 and s[l] == s[r]:
                print(l, r)
                count += 1
                l -= 1
                r += 1
            return

        dp = [[None for j in range(n)] for i in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return count


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = 0

        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1

        return res
