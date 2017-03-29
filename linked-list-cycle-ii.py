# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        runner = head
        walker = head
        is_cycle = False
        while runner.next is not None and runner.next.next is not None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                is_cycle = True
                break
        if not is_cycle:
            return None
        walker = head
        while walker != runner:
            walker = walker.next
            runner = runner.next
        return walker

t = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
h = ListNode(0)
p = h.next
for i in t:
    p = ListNode(i)
    p = p.next
p = h.next
r = Solution().detectCycle(p)

