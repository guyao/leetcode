"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution0(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pi = 0
        preceding_element = None
        dot = False
        for i, v in enumerate(s):
            if pi >= len(p):
                return False
            print(i,v, p[pi], preceding_element)
            if p[pi] == "*":
                if preceding_element is None:
                    return False
                if preceding_element == v:
                    pass
            elif p[pi] == ".":
                pi += 1
            elif p[pi] == v:
                if dot:
                    dot = False
                pi += 1
            else:
                return False
            preceding_element = v
        return True



class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        i = 0
        j = 0
        dp[0][0] = True

        for i in range(2, n + 1):
            dp[0][i] = dp[0][i-1] and p[i-1] == "*"
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == "*":
                    dp[i][j] = (i>0)\
                        and (p[j-2] == s[i-1] or p[j-2] == '.') \
                        and (dp[i-1][j]) \
                        or (dp[i][j-2])
                else:
                    dp[i][j] = i > 0 \
                        and dp[i-1][j-1] \
                        and (s[i-1] == p[j-1] \
                            or p[j-1] == ".")
        return dp[m][n]







# assert Solution().isMatch("aa","a") == False
# assert Solution().isMatch("aa","aa") == True
# assert Solution().isMatch("aaa","aa") == False
# assert Solution().isMatch("aaa","aa") == False
assert Solution().isMatch("aa", "a*") == True
# assert Solution().isMatch("aa", ".*") == True
# assert Solution().isMatch("ab", ".*") == True
# assert Solution().isMatch("aab", "c*a*b") == True
# assert Solution().isMatch("ba", "ba*") == True

