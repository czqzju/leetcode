# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0

        nums = []
        nums.append(root.val)
        res = 0
        if (root.left is None and root.right is None):
            for i in range(len(nums) - 1, -1, -1):
                res += nums[i] * 10 ** (len(nums) - 1 - i)
            nums.pop(-1)
            return res
        if(root.left is not None):
            res += self.calcSum(nums, root.left)
        if(root.right is not None):
            res += self.calcSum(nums, root.right)

        return res

    def calcSum(self, nums, root):
        nums.append(root.val)
        res = 0
        if(root.left is None and root.right is None):
            for i in range(len(nums) - 1, -1, -1):
                res += nums[i] * 10 ** (len(nums) - 1 - i)
            nums.pop(-1)
            return res
        if (root.left is not None):
            res += self.calcSum(nums, root.left)
        if (root.right is not None):
            res += self.calcSum(nums, root.right)

        nums.pop(-1)
        return res
