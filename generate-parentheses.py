class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ret = []
        self.addparathese("", n, 0)
        return self.ret
        

    def addparathese(self, s, m, n):
        if m == 0 and n == 0:
            self.ret.append(s)
            return 
        if n > 0:
            self.addparathese(s+")", m, n - 1)
        if m > 0:
            self.addparathese(s+"(", m - 1, n + 1)

r = Solution().generateParenthesis(3)
