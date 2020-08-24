# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        if not root:
            return self.sum
        if root.left:
            self.dfs(root.left, True)
        if root.right:
            self.dfs(root.right, False)
        return self.sum

    def dfs(self, root: TreeNode, isLeft: bool) -> None:
        if isLeft and not root.left and not root.right:
            self.sum += root.val

        if root.left:
            self.dfs(root.left, True)
        if root.right:
            self.dfs(root.right, False)

root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(Solution().sumOfLeftLeaves(root))