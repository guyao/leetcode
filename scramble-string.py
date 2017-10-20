# Time Limit Exceeded
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        length = len(s1)
        if length == 1:
            return s1 == s2
        result = False
        for i in range(1, length):
            s1l = s1[:i]
            s1r = s1[i:]
            s2l1 = s2[:i]
            s2r1 = s2[i:]
            s2l2 = s2[-i:]
            s2r2 = s2[:-i]
            if self.isScramble(s1l, s2l1) and self.isScramble(s1r, s2r1):
                return True
            if self.isScramble(s1l, s2l2) and self.isScramble(s1r, s2r2):
                return True
        return result


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        dp = [[[None for k in range(length + 1)]
               for j in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True
                else:
                    dp[i][j][1] = False

        def search(x, y, k):
            if dp[x][y][k] is not None:
                return dp[x][y][k]
            result = False
            for i in range(1, k):
                result = result or (search(x, y, i) and search(
                    x + i, y + i, k - i)) or (search(x, y + k - i, i) and search(x + i, y, k - i))
                if result == True:
                    dp[x][y][k] = True
                    return True
            dp[x][y][k] = False
            return False
        return search(0, 0, length)


s1 = "great"
s2 = "rgtae"
# expect True
s1 = "abcdefghijklmn"
s2 = "efghijklmncadb"
# expect False
r = Solution().isScramble(s1, s2)
print(r)
