class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        import collections
        q = collections.deque([kill])
        m = collections.defaultdict(list)
        res = []
        for parent, children in zip(ppid, pid):
            m[parent].append(children)
        while q:
            node = q.popleft()
            res.append(node)
            for n in m[node]:
                q.append(n)
        return res