# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p1 = head
        p2 = head.next if head is not None else None
        head1 = p1
        head2 = p2
        while p1 and p2:
            p1.next = p2.next
            p1 = p2.next

            p2.next = p1.next if p1 is not None else None
            p2 = p1.next if p1 is not None else None

        tail = head
        while tail.next is not None:
            tail = tail.next

        tail.next = head2
        return head