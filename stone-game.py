# https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        N = len(piles)

        def search(i, j):
            if i > j:
                return 0
            parity = (j - i - N) % 2
            if parity == 1:
                return max(piles[i] + search(i + 1, j), piles[j] + search(i, j - 1))
            else:
                return min(-piles[i] + search(i + 1, j), -piles[j] + search(i, j - 1))
        return search(0, N - 1) > 0