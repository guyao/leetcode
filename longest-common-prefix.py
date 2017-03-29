class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        main = strs[0]
        p = 0
        for i in range(len(main)):
            current = main[i]
            for s in strs[1:]:
                if i < len(s):
                    if s[i] != current:
                        return main[:i]
                else:
                    return main[:i]
        return main


r = Solution().longestCommonPrefix(["aa", "a"])
# r = Solution().longestCommonPrefix(["a"])


