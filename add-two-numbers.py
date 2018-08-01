# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        h = ListNode(None)
        p = h
        p1 = head1
        p2 = head2
        carry = 0
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            v = v1 + v2

            if carry:
                v += 1
                carry = 0
            carry = v // 10
            v = v % 10

            p.next = ListNode(v)

            p = p.next
            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2

        if carry:
            p.next = ListNode(1)
        return h.next