# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict, deque
        value_map = defaultdict(dict)
        for equation, value in zip(equations, values):
            x, y = equation
            value_map[x][y] = value
            value_map[y][x] = 1 / value

        def bfs(start, target):
            queue = deque([(start, 1)])
            seen = set()
            while queue:
                e, val = queue.popleft()
                seen.add(e)
                for k, v in value_map[e].items():
                    if k == target:
                        return val * v
                    elif k not in seen:
                        queue.append((k, val * v))
            return -1

        return [bfs(*q) for q in queries]