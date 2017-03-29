# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) < 1:
            return None
        root_value = preorder[0]
        root_index = inorder.index(root_value)
        r = TreeNode(root_value)
        r.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
        r.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])
        return r


"""
   0
  1 2
3 4 5 6

preorder  : 0 1 3 4 2 5 6
inorder   : 3 1 4 0 5 2 6
postorder : 3 4 1 5 6 2 0
"""
preorder = [0, 1, 3, 4, 2, 5, 6]
inorder = [3, 1, 4, 0, 5, 2, 6]
r = Solution().buildTree(preorder, inorder)
