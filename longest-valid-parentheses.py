class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ps = []
        note = [0 for _ in range(len(s))]
        for i, c in enumerate(s):
            if c == ")":
                if len(ps) > 0:
                    if ps[-1][0] == "(":
                        _, idx = ps.pop()
                        note[idx] = 1
                        note[i] = 1
                    else:
                        ps.append((c, i))
                else:
                    ps.append((c, i))
            else:
                ps.append((c, i))
        maxhere = 0
        maxsofar = 0
        for i in range(len(s)):
            if note[i] == 1:
                maxhere += 1
            else:
                maxhere = 0
            maxsofar = max(maxsofar, maxhere)
        return maxsofar


s = ")()()"  # expect 4
s = "()(()" # expect 2
r = Solution().longestValidParentheses(s)
print(r)
