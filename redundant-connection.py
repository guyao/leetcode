class UnionFind:
    def __init__(self):
        self.set = [i for i in range(1000 + 1)]

    def find(self, x):
        if self.set[x] != x:
            self.set[x] = self.find(self.set[x])
        return self.set[x]

    def union(self, x, y):
        x_root, y_root = map(self.find, (x, y))
        if x_root != y_root:
            self.set[max(x_root, y_root)] = min(x_root, y_root)

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        u = UnionFind()
        for e in edges:
            x, y = e
            x_root = u.find(x)
            y_root = u.find(y)
            if x_root == y_root:
                return e
            u.union(x, y)