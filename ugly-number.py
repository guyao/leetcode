class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        candidates = [2, 3, 5]
        def helper(n):
            if n == 0:
                return False
            if n == 1:
                return True
            for prime in candidates:
                if n % prime == 0:
                    if helper(n // prime):
                        return True

        return True if helper(num) else False