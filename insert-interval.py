"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        r = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                r.append(intervals[i])
            i += 1
        r.append(Interval(start, end))
        r += intervals[i:]
        return r

def list_to_interval(l):
    r = []
    for i in l:
        r.append(Interval(i[0], i[1]))
    return r

def interval_to_list(l):
    r = []
    for i in l:
        r.append([i.start, i.end])
    return r

t = [[1,2], [3,5], [6,7], [8,10], [12,16]]
t = [[1,5]]
i_l = list_to_interval(t)
newInterval = Interval(4, 9)
# newInterval = Interval(2, 7)
newInterval = Interval(2, 3)
t = Solution().insert(i_l, newInterval)
t = interval_to_list(t)