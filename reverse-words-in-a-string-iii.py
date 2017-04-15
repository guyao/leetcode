class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i, v in enumerate(s):
            s[i] = s[i][::-1]
        s = " ".join(s)
        return s
