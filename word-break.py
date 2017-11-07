# Word Break
# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ws = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in ws and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]