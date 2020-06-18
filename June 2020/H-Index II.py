class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        start = 0
        end = n - 1
        while(start <= end):
            curIdx = (start + end) // 2
            if(citations[curIdx] == n - curIdx):
                return n - curIdx
            elif(citations[curIdx] < n - curIdx):
                start = curIdx + 1
            else:
                end = curIdx - 1
        return n - start