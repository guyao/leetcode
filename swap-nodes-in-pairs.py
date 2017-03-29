# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        h = head
        while h is not None and h.next is not None:
            curr = h
            h = h.next
            nxt = h.next
            h.next = curr
            prev.next = h
            curr.next = nxt
            prev = curr
            h = nxt
        return dummy.next



