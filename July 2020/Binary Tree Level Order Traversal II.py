# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        res = []
        curNodes = [root]

        while len(curNodes):
            children = []
            tmpValues = []
            for node in curNodes:
                tmpValues.append(node.val)
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            res.insert(0, tmpValues)
            curNodes = children
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrderBottom(root))
