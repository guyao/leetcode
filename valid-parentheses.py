class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        m = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) > 0:
                    last = stack.pop()
                    if last == m[c]:
                        continue
                    else:
                        return False
                else:
                    return False
                
        return True if len(stack) == 0 else False


r = Solution().isValid("]")