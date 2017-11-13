# Word Break II
# https://leetcode.com/problems/word-break-ii
"""
Hint:
Before DFS, verify that s could be break to pass the test case
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
        wd = set(wordDict)
        can_break = [False for _ in range(len(s) + 1)]
        can_break[0] = True
        length = len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wd and can_break[j]:
                    can_break[i] = True

        def dfs(s, st, path):
            if st == length:
                result.append(" ".join(path))
            for ed in range(st + 1, length + 1):
                if s[st:ed] in wd and can_break[st]:
                    dfs(s, ed, path + [s[st:ed]])
        if can_break[-1]:
            dfs(s, 0, [])
        return result
