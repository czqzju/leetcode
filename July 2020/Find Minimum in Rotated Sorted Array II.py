from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        curMin = nums[0]

        for num in nums:
            if num < curMin:
                curMin = num
                break

        return curMin

print(Solution().findMin([2,2,2,0,1]))