from itertools import chain, combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [x for x in map(list, chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))]



print(Solution().subsets([1,2,3]))