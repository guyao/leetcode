class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        current = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            current += diff
            total += diff
            if current < 0:
                start = i + 1
                current = 0
        if total >= 0:
            return start
        return -1