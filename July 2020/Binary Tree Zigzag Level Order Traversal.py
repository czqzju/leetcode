from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        parents = [root]
        reverseFlag = False
        while len(parents):
            children = []
            curLevelValues = []
            for parent in parents:
                curLevelValues.append(parent.val)
                if parent.left : children.append(parent.left)
                if parent.right : children.append(parent.right)

            if reverseFlag: curLevelValues.reverse()
            reverseFlag = not reverseFlag
            res.append(curLevelValues)
            del parents
            parents = children

        return res


root = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))

print(Solution().zigzagLevelOrder(root))