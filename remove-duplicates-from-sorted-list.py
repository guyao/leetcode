class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        p = dummy
        while p is not None:
            while p.next is not None and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return dummy.next