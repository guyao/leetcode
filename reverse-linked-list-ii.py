"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        h = head
        prev = None
        for i in range(m-1):
            prev = h
            h = h.next
        before = prev
        ed = h
        
        prev = None
        for i in range(n - m + 1):
            curr = h
            h = h.next
            curr.next = prev
            prev = curr
        
        ret = None
        if before is None:
             ret = prev
        else:
            before.next = prev
            ret = head
        ed.next = h
        return ret


def list_to_listnode(l):
    dummy = ListNode(0)
    p = dummy
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return dummy.next

def traverse_linked_list(l):
    p = l
    while p is not None:
        print(p.val)
        p = p.next

t = list_to_listnode([1,2,3,4,5,6,7,8,9,10])
t = list_to_listnode([3, 5,7])
t = list_to_listnode([5])
r = Solution().reverseBetween(t, 1, 1)
r
# traverse_linked_list(r)