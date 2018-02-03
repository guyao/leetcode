class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = list(filter(lambda d: bool(d),path.split("/")))
        tree = []
        for d in dirs:
            if d == ".":
                pass
            elif d == "..":
                if tree:
                    tree.pop()
            else:
                tree.append(d)
        path ="/" + "/".join(tree)
        return path