from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startPos = []
        for i in range(len(intervals)):
            startPos.append([intervals[i][0], i])
        startPos.sort(key=lambda x : x[0])

        starts = []
        pos = []
        for item in startPos:
            starts.append(item[0])
            pos.append(item[1])

        res = []
        for interval in intervals:
            indexRightIntervel = bisect.bisect_left(starts, interval[1])
            if indexRightIntervel >= len(starts):
                res.append(-1)
            else:
                res.append(pos[indexRightIntervel])
        return res


print(Solution().findRightInterval([ [3,4]]))