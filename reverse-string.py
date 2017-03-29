class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        end = len(s) - 1
        for i in range(end // 2 + 1):
            print(i)
            s[i], s[end - i] = s[end - i], s[i]
        return ''.join(s)

r = Solution().reverseString("world!")
print(r)


