class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        c2i = {c:i for c, i in zip("0123456789", range(10))}
        def str2int(s):
            res = 0            
            for c in s:
                res = res * 10
                res += c2i[c]
            return res
        return str(str2int(num1) * str2int(num2))