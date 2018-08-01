class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        N = len(profit)
        MOD = 10 ** 9 + 7

        dp = [[[0 for k in range(G + 1)]
                  for j in range(P + 1)]
                  for i in range(N + 1)]
        
        dp[0][0][0] = 1
        
        for i in range(1, N + 1):
            idx = i - 1
            p = profit[idx]
            g = group[idx]
            for j in range(P + 1):
                for k in range(G + 1):
                    if k - g >= 0:
                        dp[i][j][k] += dp[i-1][max(0, j - p)][k - g] % MOD
                    dp[i][j][k] += dp[i-1][j][k] % MOD
        return sum(dp[-1][-1]) % MOD
