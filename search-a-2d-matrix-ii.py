#The saddle back search 
#EWD-934 http://www.cs.utexas.edu/users/EWD/ewd09xx/EWD934.PDF
"""
- If f(p, q) < z, since f is strict increasing, for all 0 ≤ y < q, we have f(p, y) < z. We can drop all points in the vertical line section (in red color);
- If f(p, q) > z, then f(x, q) > z for all p < x ≤ z. We can drop all points in the horizontal line section (in blue color);
- Otherwise if f(p, q) = z, we mark (p, q) as one solution, then both line sections can be dropped.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        x, y = 0, len(matrix[0]) - 1
        while y >= 0 and x <= len(matrix)-1:
            v = matrix[x][y]
            if v < target:
                x += 1
            elif v > target:
                y -= 1
            else:
                return True
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 11
r = Solution().searchMatrix(matrix, target)
print(r)