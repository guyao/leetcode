"""
dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
dp[i][i]
dp[i][i+1] if 
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[None if i != j else 1 for i in range(len(s))] for j in range(len(s))]
        maxlen = 0
        maxi = 0
        maxj = 0
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = 2
                maxi = i - 1
                maxj = i
        for i in reversed(range(len(s))):
            for j in range(len(s)):
                if i + 1 < len(s) and j - 1 > 0 and (i <= j) and (i + 1 <= j - 1):
                    if (s[i] == s[j]) and (dp[i+1][j-1] is not None):
                        dp[i][j] = dp[i+1][j-1] + 2
                        if dp[i][j] > maxlen:
                            maxlen = dp[i][j]
                            maxi = i
                            maxj = j
        return s[maxi:maxj+1]

# r = Solution().longestPalindrome("werabbao")
# r = Solution().longestPalindrome("a")
# r = Solution().longestPalindrome("bb")
r = Solution().longestPalindrome("abcda")