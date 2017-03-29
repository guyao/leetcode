# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# heap
# O(nk lg k) runtime, O(k) space - Heap

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        import heapq
        dummy = ListNode(0)
        p = dummy
        for l in lists:
            if l is not None:
                heapq.heappush(h, (l.val, l))
        while len(h) > 0:
            v, l = heapq.heappop(h)
            p.next = l
            p = p.next
            if l.next is not None:
                heapq.heappush(h, (l.next.val ,l.next))
        return dummy.next

# O(nk lg k) runtime, O(1) space - Divider and Conquer 
# using two way merge
"""
Merge two list at a time, number of list reduce from
k->k/2->k/4...1

size of the list:
n->2n->4n...2^(log k)n

runtime complexity:
nk*log k
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2lists(l1, l2):
            dummy = ListNode(0)
            p = dummy
            while (l1 != None) and (l2 != None):
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1 != None:
                p.next = l1
            if l2 != None:
                p.next = l2
            return dummy.next
            lower = 0
        upper = len(lists) - 1
        while upper > 0:
            lower = 0
            while lower < upper:
                lists[lower] = merge2lists(lists[lower], lists[upper])
                lower += 1
                upper -= 1
        r = lists[0] if len(lists) > 0 else lists
        return r


t1 = [1, 3, 5, 7]
t2 = [2, 4, 6, 8]

def list_to_linked_list(l):
    result = ListNode(0)
    p = result
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return result.next
t1 = list_to_linked_list(t1)
t2 = list_to_linked_list(t2)
r = Solution().mergeKLists([t1, t2])
r = Solution().mergeKLists([None])


