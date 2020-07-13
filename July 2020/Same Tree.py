# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val != q.val: return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False

t1 = TreeNode(1,
              left = TreeNode(2),
              right = TreeNode(3))

t2 = TreeNode(1,
              left = TreeNode(2),
              right = TreeNode(3))

t3 = TreeNode(1,
              left = TreeNode(3),
              right = TreeNode(2))

print(Solution().isSameTree(t1, t3))
