class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1) - 1
        n = len(num2) - 1
        if m > n:
            m, n, num1, num2 =  n, m, num2, num1
        res = 0
        add = False
        i = 0
        for i in range(m+1):
            digit = int(num1[m - i]) + int(num2[n - i])
            if add:
                digit += 1
                add = False
            if digit // 10:
                add = True
            digit = digit % 10
            res = res + (10**i)*digit
        i += 1
        res += 10**i if add else 0
        if num2[:n+1-i]:
            res += int(num2[:n+1-i])*(10**i)
        return str(res)
n1 = "11123"
n2 = "29"
n1 = "1"
n2 = "9"
r = Solution().addStrings(n1, n2)
print(r)