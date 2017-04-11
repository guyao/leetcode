class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-','')
        size = len(S)
        fst = size % K
        if not fst:
            fst = K
        res = []
        res.append(S[:fst])
        index = fst
        while index < size:
            res.append(S[index:index+K])
            index += K
        return '-'.join(res)

s = "2-4A0r7-4k"
k = 4
Solution().licenseKeyFormatting(s, k)