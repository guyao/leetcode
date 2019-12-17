# DFS, recursive

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        seen = set()
        # num of rows
        m = len(grid)
        # num of cols
        n = len(grid[0])
        
        
        def dfs(i, j):
            if (0 <= i < m) and (0 <= j < n) and grid[i][j] and (i, j) not in seen:
                seen.add((i, j))
                return 1 + sum([dfs(i + dx, j + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]])
            else:
                return 0
        
        return max([dfs(i, j) for i in range(m) for j in range(n)])

# DFS, iterative
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        seen = set()
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if ((i, j) not in seen) and (grid[i][j]):
                    # do dfs
                    stack = [(i, j)]
                    seen.add((i, j))
                    area = 0
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0 <= (r + dr) < m and 0 <= (c + dc) < n and (grid[r + dr][c + dc]) and (r + dr, c + dc) not in seen:
                                stack.append((r + dr, c + dc))
                                seen.add((r + dr, c + dc))
                    ans = max(ans, area)
        return ans
