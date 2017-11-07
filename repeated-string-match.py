#https://leetcode.com/problems/repeated-string-match/
"""
T += A until T >= A + B
upperbound of T
(len(T) - 1) / len(A) + 1
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a = list(A)
        b = list(B)
        import copy
        t = copy.copy(a)
        while len(t) < len(b) + len(a):
            t += a
        t = "".join(t)
        b = "".join(b)
        try:
            n = t.index(b)
            return (n + len(b) - 1)//len(a) + 1
        except ValueError:
            return -1