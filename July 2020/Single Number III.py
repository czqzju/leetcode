from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        s = set(nums)
        for num in s:
            nums.remove(num)
        return list(s.difference(set(nums)))


print(Solution().singleNumber([1,2,1,3,2,5]))