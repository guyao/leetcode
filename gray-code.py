class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(n):
            if n == 0:
                return ["0"]
            if n == 1:
                return ["0", "1"]
            result = helper(n-1)
            return ["0" + code for code in result] + ["1" + code for code in reversed(result)]
        return [int(s, base=2) for s in helper(n)]