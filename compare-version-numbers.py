class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in range(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in range(len(v2) - len(v1))]

        while v1 and v2:
            n1 = int(v1.pop(0))
            n2 = int(v2.pop(0))
            if n1 != n2:
                return 1 if n1 > n2 else -1
        if v1:
            return 1
        if v2:
            return -1
        return 0