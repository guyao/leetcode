# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import collections
        max_points = 0
        for i, start in enumerate(points):
            slope_count, same = collections.defaultdict(int), 1
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    slope = float("inf")
                    if start.x - end.x != 0:
                        gcd = lambda x, y: x if y == 0 else gcd(y, x%y)
                        y = start.y - end.y
                        x = start.x - end.x
                        gcdn = gcd(y, x)
                        slope = ((y/gcdn),(x/gcdn))

                        # slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    slope_count[slope] += 1
            
            current_max = same            
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)
                
            max_points = max(max_points, current_max)
            
        return max_points

ps = [
    [0,0],
    [0,1],
    [0,2],
    [0,3],
    [1,1],
    [4,5]
]
ps =[[0,0],[94911151,94911150],[94911152,94911151]]
t = []
for p in ps:
    t.append(
        Point(p[0],p[1])
        )
r = Solution().maxPoints(t)