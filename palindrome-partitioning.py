# Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        res = []

        def dfs(s, st, path, res):
            if st == len(s):
                res.append(path[:])
            for i in range(st + 1, len(s) + 1):
                if self.isPalindrome(s[st:i]):
                    path.append(s[st:i])
                    dfs(s, i, path, res)
                    path.pop()
        dfs(s, 0, path, res)
        return res

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
