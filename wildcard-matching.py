class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != "*":
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == "?")
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]