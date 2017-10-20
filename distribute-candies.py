class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        from collections import Counter
        from itertools import cycle
        c = Counter()
        c.update(candies)
        l = [c[i] for i in c]
        l.sort()
        count = 0
        start_index = 0
        kinds = set()
        for i in cycle(range(len(l))):
            if count >= len(candies) // 2:
                break
            if i < start_index:
                continue
            kinds.add(i)
            count += 1
            l[i] -= 1
            if l[i] == 0:
                start_index += 1
        return len(kinds)

def distributeCandies(self, candies):
    return min(len(candies) / 2, len(set(candies)))




t = [1,1,2,2,3,3]
r = Solution().distributeCandies(t)
print(r)