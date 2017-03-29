# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        for i in range(n):
            p = p.next
        q = head
        prev = ListNode(None)
        while p is not None:
            p = p.next
            prev = q
            q = q.next
        prev.next = q.next if q.next is not None else None
        return head

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
r = Solution().removeNthFromEnd(ListNode(1), 1)
