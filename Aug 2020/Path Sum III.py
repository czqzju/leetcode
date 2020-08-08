from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.cnt = 0
        if root.val == sum:
            self.cnt += 1
        if root.left:
            self.dfs(root.left, sum, [root.val])
        if root.right:
            self.dfs(root.right, sum, [root.val])

        return self.cnt


    def dfs(self, root: TreeNode, sum: int, preSums: List):
        if root.val == sum:
            self.cnt += 1
        for i in range(len(preSums)):
            if root.val + preSums[i] == sum:
                self.cnt += 1
            preSums[i] += root.val
        if root.left:
            self.dfs(root.left, sum, preSums + [root.val])
        if root.right:
            self.dfs(root.right, sum, preSums + [root.val])



root = TreeNode(10,
                left=TreeNode(5,
                              left=TreeNode(3,
                                            left=TreeNode(3),
                                            right=TreeNode(-2)),
                              right=TreeNode(2,
                                             right=TreeNode(1))),
                right=TreeNode(-3,
                               right=TreeNode(11)))

print(Solution().pathSum(root, 8))