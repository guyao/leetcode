# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        def reverse(head):
            prev = None
            p = head
            while p is not None:
                t = p.next
                p.next = prev
                prev = p
                p = t
            return prev
        dummy = ListNode(None)
        dummy.next = head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        l1 = dummy.next
        l2 = reverse(slow.next)

        slow.next = None

        while l1 is not None and l2 is not None:
            l1next = l1.next        
            l2next = l2.next
            l1.next = l2
            l2.next = l1next
            l1 = l1next
            l2 = l2next
        