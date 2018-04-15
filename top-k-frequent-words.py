from heapq import heappush, heappop, heapify
from itertools import groupby

class max_heap:
    def __init__(self, data=[]):
        self.heap = [(-freq, c) for freq, c in data]
        heapify(self.heap)


    def push(self, x):
        heappush(self.heap, -x)

    def pop(self):
        v = heappop(self.heap)
        return (-v[0], v[1])

    def non_empty(self):
        return bool(self.heap)


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        counter = Counter(words)
        heap = max_heap([(counter[key], key) for key in counter])
        result = []
        for _ in range(k):
            v = heap.pop()
            result.append(v)

        while True and heap.non_empty():
            v = heap.pop()
            if v[0] == result[-1][0]:
                result.append(v)
            else:
                break

        res = []
        for group in groupby(result, lambda x: x[0]):
            res += sorted([element[1] for element in group[1]])
        return res[:k]