class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bk = set(bank)
        n = len(start)
        visited = set()
        curr = [start]
        dis = 0
        while curr:
            nxt = []
            for gen in curr:
                if gen == end:
                    return dis
                for i in range(n):
                    for g in "ACGT":
                        candidate = gen[:i] + g + gen[i + 1:]
                        if candidate in bk and candidate not in visited:
                            nxt.append(candidate)
                            visited.add(candidate)
            curr = nxt
            dis += 1
        return -1
