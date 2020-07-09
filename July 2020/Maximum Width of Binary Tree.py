# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = 0
        root.val = 0
        curLevel = [root]
        while len(curLevel):
            children = []
            tmp = curLevel[-1].val - curLevel[0].val + 1
            res = tmp if tmp > res else res
            for node in curLevel:
                if node.left:
                    node.left.val = node.val * 2
                    children.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 1
                    children.append(node.right)
            curLevel = children
        return res




root = TreeNode(1,
                TreeNode(3, TreeNode(5), TreeNode(3)),
                TreeNode(2, right=TreeNode(9)))

print(Solution().widthOfBinaryTree(root))