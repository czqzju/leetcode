import bisect
from collections import Counter
from copy import deepcopy

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        return [[x[0], x[1], x[2]] for x in res]




print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))