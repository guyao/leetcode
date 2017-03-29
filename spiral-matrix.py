"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

"""
n
m - 1
n - 1
m - 2
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = []
        if len(matrix) == 0:
            return r
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = -1
        m -= 1
        while True:
            for i in range(n):
                col += 1
                # print(row,col)
                r.append(matrix[row][col])
            n -= 1
            if m == 0:
                break

            for i in range(m):
                row += 1
                # print(row,col)
                r.append(matrix[row][col])
            m -= 1
            if n == 0:
                break

            for i in range(n):
                col -= 1
                # print(row, col)
                r.append(matrix[row][col])

            n -= 1
            if m == 0:
                break

            for i in range(m):
                row -= 1
                # print(row, col)
                r.append(matrix[row][col])

            m -= 1
            if n == 0:
                break
        return r




t = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
t = [
    [1,2],
    [3,4]
]
t = []
r = Solution().spiralOrder(t)