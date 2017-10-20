#Union Find
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid):
            return 0
        ht = len(grid)
        wd = len(grid[0])
        uf = [i for i in range(ht*wd)]
        def find(x):
            p = uf[x]
            while p != uf[p]:
                p = uf[p]
            top = p
            t = -1
            p = x
            while p != uf[p]:
                t = uf[p]
                uf[p] = top
                p = t
            return top
        def union(x, y):
            p_x, p_y = find(x), find(y)
            if p_x != p_y:
                uf[p_x] = p_y
        def index(x, y):
            return x*wd + y
        def search(x, y):
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < ht and 0 <= j < wd:
                    if grid[i][j] == "1":
                        union(index(i, j), index(x, y))
        for i in range(ht):
            for j in range(wd):
                if grid[i][j] == "1":
                    search(i, j)
        for i in range(ht):
            for j in range(wd):
                if grid[i][j] == "1":
                    find(i*wd+j)
        result = set()
        for i in range(ht):
            for j in range(wd):
                if grid[i][j] == "1":
                    result.add(uf[index(i,j)])
        return len(result)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid):
            return 0
        ht = len(grid)
        wd = len(grid[0])
        count = 0
        m = [list(l) for l in grid]
        def dfs(i, j):
            if 0 <= i < ht and 0 <= j < wd and m[i][j] == "1":
                m[i][j] = "0"
                for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    dfs(ii, jj)
            else:
                return
        for i in range(ht):
            for j in range(wd):
                if m[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


t = ["11110","11010","11000","00000"]
t = ["11000", "11000", "00100", "00011"]
r = Solution().numIslands(t)