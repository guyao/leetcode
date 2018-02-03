class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col_corner = 1
        row_corner = 1
        for i in range(m):
            if matrix[i][0] == 0:
                col_corner = 0
        for j in range(n):
            if matrix[0][j] == 0:
                row_corner = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in reversed(range(1, m)):
            for j in reversed(range(1, n)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_corner == 0:
            for i in range(m):
                matrix[i][0] = 0
        if row_corner == 0:
            for j in range(n):
                matrix[0][j] = 0