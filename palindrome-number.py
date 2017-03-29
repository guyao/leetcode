"""
while x/div >= 10:
    div = div * 10
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        div = 1
        while x / div >= 10:
            div = div * 10
            print(div)
        while x != 0:
            r = x % 10
            l = x // div
            print(l, r, x, div)
            if l != r:
                return False
            x = x % div
            x = x // 10
            div = div // 100
        return True

r = Solution().isPalindrome(1001)
print(r)
# print(isPalindrome(1001))