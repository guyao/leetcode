class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = ListNode(None)
        larger = ListNode(None)
        sp = smaller
        lp = larger
        p = head
        while p is not None:
            nxt = p.next
            if p.val < x:
                sp.next = p
                sp = sp.next
                sp.next = None
            else:
                lp.next = p
                lp = lp.next
                lp.next = None
            p = nxt
        sp.next = larger.next
        return smaller.next