# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return str(self.label)

# Depth First traversal
"""
Note that the graph could contain cycles, for example a node could have a neighbor that points back to it. Therefore, we should use a map that records each node’s copy to avoid infinite recursion.
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        self.m = {}
        return self.DFS(node)

    def DFS(self, node):
        if self.m.get(node):
            return self.m.get(node)
        copy = UndirectedGraphNode(node.label)
        self.m[node] = copy
        for adj in node.neighbors:
            copy.neighbors.append(self.DFS(adj))
        return copy


# Breadth traversal2
"""
A straight forward breadth-first traversal seemed to work. But some details are still missing. For example, how do we connect the nodes of the cloned graph?
The fact that B can traverse back to A implies that the graph may contain a cycle. You must take extra care to handle this case or else your code could have an infinite loop.
A <-> B
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        q = []
        h = {}
        ret = UndirectedGraphNode(node.label)
        h[node] = ret
        q.append(node)
        while len(q) > 0:
            n = q.pop(0)
            for adj in n.neighbors:
                if h.get(adj) is None:
                    copy = UndirectedGraphNode(adj.label)
                    h[adj] = copy
                    q.append(adj)
                else:
                    copy = h[adj]
                h[n].neighbors.append(copy)
        return ret


t = UndirectedGraphNode(1)
t.neighbors = [UndirectedGraphNode(2), \
                UndirectedGraphNode(3)]
t.neighbors[0].neighbors.append(UndirectedGraphNode(4))
t.neighbors[1].neighbors.append(UndirectedGraphNode(5))
t.neighbors[1].neighbors[0].neighbors.append(t)

r = Solution().cloneGraph(t)
