class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        LENGTH = 10
        visited = set()
        res = set()
        for i in range(len(s) + 1 - LENGTH):
            subs = s[i:i+LENGTH]
            if subs in visited:
                res.add(subs)
            visited.add(subs)
        return list(res)