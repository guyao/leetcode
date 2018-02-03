class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next is not None and p.next.next is not None:
            if p.next.val == p.next.next.val:
                v = p.next.val
                while p.next.next is not None and p.next.next.val == v:
                    p.next = p.next.next
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next