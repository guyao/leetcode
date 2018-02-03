class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def valid(s):
            if not (int(s) <= 255):
                return False
            if len(s) > 1 and s.startswith("0"):
                return False
            return True

        def dfs(s, path, n):
            if not s and len(path) == 4:
                res.append(path[:])
            elif len(path) > 4:
                return
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if int(cur) > 255:
                    break
                else:
                    if valid(cur):
                        dfs(s[i:], path + [cur], n + 1)
        dfs(s, [], 1)
        return [".".join(ip) for ip in res]