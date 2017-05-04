class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        m = {}
        m.update({c:1 for c in "qwertyuiop"})
        m.update({c:2 for c in "asdfghjkl"})
        m.update({c:3 for c in "zxcvbnm"})
        res = []
        for w in words:
            status = None
            valid = True
            for c in w:
                c = c.lower()
                if not status:
                    status = m[c]
                else:
                    if status == m[c]:
                        pass
                    else:
                        valid = False
            if valid:
                res.append(w)
        return res

r = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(r)