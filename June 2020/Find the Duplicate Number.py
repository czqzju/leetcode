class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if(nums.count(i) > 1):
                return i


print(Solution().findDuplicate([2,2,2,2]))