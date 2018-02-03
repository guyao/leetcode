# DFS, Time Limit Exceed
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        def dfs(s, path):
            if not s and path:
                res.append(path[:])
                return
            for i in range(1, len(s) + 1):
                n = int(s[:i])
                if 1 <= n <= 26:
                    dfs(s[i:], path + [n])
                else:
                    break
        dfs(s, [])
        return len(res)

# DP
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.startswith("0"):
            return 0
        dp = [1,1]
        for i in range(2, len(s) + 1):
            if 10 <= int(str(s[i-2:i])) <= 26 and s[i-1] != '0':
                dp.append(dp[i-1] + dp[i-2])
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])
            elif s[i-1] != "0":
                dp.append(dp[i-1])
            else:
                return 0
        return dp[-1]