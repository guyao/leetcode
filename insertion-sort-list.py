# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(None)
        cur = head
        pre = dummy
        nxt = None
        while cur is not None:
            nxt = cur.next

            while pre.next is not None and pre.next.val  < cur.val:
                pre = pre.next

            cur.next = pre.next
            pre.next = cur

            pre = dummy
            cur = nxt
        return dummy.next