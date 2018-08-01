class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def length(head):
            count = 0
            while head is not None:
                head = head.next
                count += 1
            return count

        len_A = length(headA)
        len_B = length(headB)
        diff = abs(len_A - len_B)
        if len_A > len_B:
            h1 = headA
            h2 = headB
        else:
            h1 = headB
            h2 = headA
        for _ in range(diff):
            h1 = h1.next
        while (h1 is not None) and (h2 is not None) and (h1 is not h2):
            h1 = h1.next
            h2 = h2.next
        return h1