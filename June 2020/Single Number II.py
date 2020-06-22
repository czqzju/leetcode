class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 1):
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if(i == 0 and nums[i] != nums[i + 1]):
                return nums[i]
            elif(i == len(nums) - 1 and nums[i] != nums[i - 1]):
                return nums[i]
            else:
                if(nums[i] != nums[i-1] and nums[i] != nums[i+1]):
                    return nums[i]


a = [2,2,3,2]
print(Solution().singleNumber(a))
