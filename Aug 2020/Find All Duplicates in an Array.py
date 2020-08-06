from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        setNums = set()
        res = []
        for num in nums:
            if num in setNums:
                res.append(num)
            setNums.add(num)
        return res
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))