class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {c:False for c in s}
        j = 0
        ans = 0
        for i in range(len(s)):
            while j < len(s) and not m[s[j]]:
                m[s[j]] = True
                ans = max(ans, j - i + 1)
                j += 1
            m[s[i]] = False
        return ans