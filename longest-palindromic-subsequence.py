class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[None for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        def search(l, r):
            if l <= r and l >= 0 and r <= n - 1:
                if dp[l][r] is not None:
                    return dp[l][r]
                else:
                    if s[l] == s[r]:
                        dp[l][r] = search(l + 1, r - 1) + 2
                    else:
                        dp[l][r] = max(search(l + 1, r), search(l, r - 1))
                    return dp[l][r]
            else:
                return 0
        search(0, n - 1)
        return dp[0][n - 1]
