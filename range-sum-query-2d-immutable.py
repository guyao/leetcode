class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = [[] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            s = 0
            for n in matrix[row]:
                s += n
                self.sums[row].append(s)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 == 0:
            lo = None
        else:
            lo = col1 - 1
        hi = col2
        s = 0
        for i in range(row1, row2 + 1):
            if lo is None:
                s += self.sums[i][hi]
            else:
                s += self.sums[i][hi] - self.sums[i][lo]
        return s

# O(1) calc sum
"""
sums[i][j] means sum from (0,0) to (i,j)

To calculate:
    (r1, c1) (r2, c2)
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = [[] for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            s = 0
            for j, v in enumerate(row):
                if i == 0:
                    last = 0
                else:
                    last = self.sums[i-1][j]
                s += matrix[i][j]
                self.sums[i].append(s+last)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 == 0:
            up = 0
        else:
            up = self.sums[row2][col1-1]
        if row1 == 0:
            left = 0
        else:
            left = self.sums[row1-1][col2]
        if col1 == 0 or row1 == 0:
            left_up = 0
        else:
            left_up = self.sums[row1-1][col1-1]
        res = self.sums[row2][col2] - left - up + left_up
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)

# r = obj.sumRegion(2, 1, 4, 3) # 8
# r = obj.sumRegion(1, 1, 2, 2) # 11
# r = obj.sumRegion(1, 2, 2, 4) # 12
r = obj.sumRegion(0, 0, 0, 0)
print(r)