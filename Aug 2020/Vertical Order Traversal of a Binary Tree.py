from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.posValue = []
        self.computePos(root, [0, 0])
        self.posValue.sort(key=lambda x: (x[0], -x[1], x[2]))

        res = [[]]
        curX = self.posValue[0][0]
        for item in self.posValue:
            if item[0] == curX:
                res[-1].append(item[2])
            else:
                curX = item[0]
                res.append([item[2]])
        return res

    def computePos(self, root: TreeNode, pos: List):
        pos.append(root.val)
        self.posValue.append(pos)

        if root.left:
            self.computePos(root.left, [pos[0] - 1, pos[1] - 1])
        if root.right:
            self.computePos(root.right, [pos[0] + 1, pos[1] - 1])





root = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))

print(Solution().verticalTraversal(root))
