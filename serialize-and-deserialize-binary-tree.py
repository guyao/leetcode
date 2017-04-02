# Definition for a binary tree node.
#TODO
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode("+str(self.val)+")"

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        inbox = [root]
        while inbox:
            todo = []
            while inbox:
                out = inbox.pop(0)
                lst.append(out.val if out is not None else None)
                if out is not None:
                    todo.append(out.left)
                    todo.append(out.right)
            inbox = todo
        ed = len(lst) - 1
        if not ed:
            return ""
        while lst[ed] is None:
            lst.pop()
            ed -= 1
        return ",".join(str(_) for _ in lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data.split(",")
        lst = [int(i) if i != "None" else None for i in lst]
        level = []
        level.append(lst[0])
        index = 0 + 1
        dummy_root = TreeNode(None)
        roots = [dummy_root]
        def build_level(roots, nodes):
            i = 0
            for r in roots:
                if r is None:
                    pass
                else:
                    left = nodes[i:i+1]
                    right = nodes[i+1:i+2]
                    r.left = left[0] if left else None
                    r.right = right[0] if right else None
                    i += 2

        while level:
            nodes = []
            nodes = [TreeNode(v) if v is not None else None for v in level]
            # for v in level:
                # if v is not None:
                    # nodes.append(TreeNode(v))
            ed = len(nodes) - 1
            while nodes[ed] is None:
                nodes.pop()
                ed -= 1
            build_level(roots, nodes)
            roots = nodes
            real_nodes = []
            for n in nodes:
                if n is not None:
                    real_nodes.append(n)
            count = 2 * len(real_nodes)
            nxt = lst[index:index+count]
            index = index + count
            level = nxt
        return dummy_root.left

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
