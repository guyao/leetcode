"""
Solution 
DP
O(MNN)

but Python get TLE
"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        INF = 0x11111111111111111111111111111111
        dp = [[0 for j in range(len(ring))] for i in range(len(key) + 1)]
        n = len(ring)
        m = len(key)
        for i in range(n):
            dp[0][i] = min(i, n - i)
        for i in range(1, m + 1):
            for j in range(n):
                dp[i][j] = INF
                for k in range(n):
                    if key[i-1] == ring[k]:
                        diff = abs(j - k)
                        step = min(diff, n - diff)
                        dp[i][j] = min(dp[i][j], step + dp[i-1][k])
            print(dp[i])
        return min(dp[i]) + m
"""
Solution
modified DP

O(Mnn) n is the most occurrence
"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        INF = float('inf')
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))
        # position of each char in ring
        pos = {}
        for i, c in enumerate(ring):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:
                next_state[j] = INF
                for i in state:
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)


#Test
ring = "caotmcaataijjxi"
key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
#expect 137

ring = "zubtowzbaubaenuqtxhnemqwzwfipugitympmfuzbdpwftnquvcjjwicwjpnlnqslbjjdctklzavwbymuyknpkmpvllvrddmdebp"
key = "wivhqwzdupzfwvpyznmbbmpwvwdnszujmnzctawijkpopbualjenluicyurkbwaflknmvtmqmtbbcdtdxqejfqdljeypnubguplt"
#expect 1000

ring = "godding"
key = "gd"
#expect 4



"""
Simple DFS could not solve,
Time limt exceed when key&ring are long
O len(key)**len(ring)

class Solution(object):
    def findRotateSteps(self, ring, key):
        INF = float('inf')
        self.result = []
        self.min = INF
        self.helper(ring, 0, key, 0, [])
        print(self.result)
        return min(self.result)

    def helper(self, ring, index, key, move, trace):
        if move > self.min:
            return
        if index == len(key):
            print("got", move)
            self.result.append(move)
            if move < self.min:
                self.min = move
            return
        k = key[index]
        l = len(ring)
        for i, c in enumerate(ring):
            if c == k:
                rotate = min(i, abs(i-l))
                positive = True if i <= l - i else False
                symbol = 1 if positive else -1
                cur_move = move + rotate
                cur_move += 1 #spelling
                s = ring[i:] + ring[0:i]
                self.helper(s, index+1, key, cur_move, trace + [symbol * rotate])
"""

