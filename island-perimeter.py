class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def helper(i, j):
            if grid[i][j] == 0:
                return 0
            res = 0
            res += grid[i-1][j] if i-1 >=0 else 0
            res += grid[i][j-1] if j-1 >=0 else 0
            res += grid[i+1][j] if i+1 <m else 0
            res += grid[i][j+1] if j+1 <n else 0
            return 4-res
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += helper(i, j)
        return count

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import operator
        transpose = list(map(list, zip(*grid)))
        for row in grid + transpose:
            # map(operator.ne, [0] + row, row + [0])
            print(row)
            print([0] + row)
            print(row + [0])
            print()

        
t = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
r = Solution().islandPerimeter(t)
print(r)


