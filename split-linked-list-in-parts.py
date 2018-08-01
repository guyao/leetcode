# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def get_length(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l

        p = root

        result = []

        l = get_length(root)

        length_part = l // k
        larger = l % k

        for _ in range(k):
            part_head = p
            n = length_part
            if larger:
                n += 1
                larger -= 1
            prev = None
            for i in range(n):
                prev = p
                p = p.next
            if prev:
                prev.next = None
            result.append(part_head)

        return result