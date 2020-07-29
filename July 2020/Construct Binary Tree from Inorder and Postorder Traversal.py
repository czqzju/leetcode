from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not len(inorder) or not len(postorder):
            return None
        root = TreeNode(postorder[-1])
        inorderRootPos = inorder.index(postorder[-1])
        inorderLeftNum = inorderRootPos
        inorderRightNum = len(inorder) - inorderRootPos - 1

        if inorderLeftNum == 0:
            root.left = None
        elif inorderLeftNum == 1:
            root.left = TreeNode(inorder[0])
        else:
            root.left = self.buildTree(inorder[:inorderRootPos], postorder[:inorderRootPos])

        if inorderRightNum == 0:
            root.right = None
        elif inorderRightNum == 1:
            root.right = TreeNode(inorder[-1])
        else:
            root.right = self.buildTree(inorder[inorderRootPos+1:], postorder[len(postorder)-inorderRightNum-1:len(postorder)-1])
        return root

Solution().buildTree([1,2,3,4], [3,2,4,1])