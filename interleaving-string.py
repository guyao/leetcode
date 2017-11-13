# Interleaving String
# https://leetcode.com/problems/interleaving-string


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != (len(s1) + len(s2)):
            return False
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            dp[i][0] = s1[:i] == s3[:i]
        for i in range(len(s2) + 1):
            dp[0][i] = s2[:i] == s3[:i]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                            ) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]
