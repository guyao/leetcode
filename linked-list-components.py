# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s = set(G)
        p = head
        counter = 0
        while p:
            if p.val in s:
                counter += 1
                while p and (p.val in s):
                    p = p.next
            if p:
                p = p.next
        return counter