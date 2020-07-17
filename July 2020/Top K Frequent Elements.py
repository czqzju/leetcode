from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = [ (k, v) for k, v in Counter(nums).items()]
        cnt.sort(key=lambda x: x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
