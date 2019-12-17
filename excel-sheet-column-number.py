class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {c:i + 1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        ans = 0
        for c in s:
            ans = ans * 26 + m[c]
        return ans