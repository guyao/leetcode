from heapq import heappush, heappop
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not any(heightMap):
            return 0
        ht = len(heightMap)
        wd = len(heightMap[0])
        visit = [[0 for j in range(wd)] for i in range(ht)]
        hp = []
        self.level = 0
        self.water = 0

        for i in [0, ht-1]:
            for j in range(wd):
                heappush(hp, (heightMap[i][j], (i, j)))
                visit[i][j] = 1
        for i in range(1, ht-1):
            for j in [0, wd-1]:
                heappush(hp, (heightMap[i][j], (i, j)))
                visit[i][j] = 1


        def search(x, y):
            if heightMap[x][y] > self.level:
                self.level = heightMap[x][y]
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<=i<ht and 0<=j<wd:
                    if visit[i][j] == 0:
                        heappush(hp, (heightMap[i][j], (i, j)))
                        if self.level > heightMap[i][j]:
                            self.water += self.level - heightMap[i][j]
                        visit[i][j] = 1
        while hp:
            v, (x, y) = heappop(hp)
            search(x, y)
        return self.water

t = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
] #expetc 4
t = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]] #expect 14
r = Solution().trapRainWater(t)
print(r)