from typing import List
from copy import deepcopy
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.res = []
        curNums = []
        for i in range(0, 10):
            if N > 1 and i == 0:
                continue
            curNums.append(i)
            self.DFS(curNums, N, K)
            curNums.pop(len(curNums) - 1)

        return self.res

    def DFS(self, curNums: List, N: int, K: int):
        if len(curNums) == N:
            self.res.append(int("".join(map(str, curNums))))
            return

        if curNums[-1] + K >= 0 and curNums[-1] + K <= 9:
            curNums.append(curNums[-1] + K)
            self.DFS(curNums, N, K)
            curNums.pop(len(curNums) - 1)

        if K != 0:
            if curNums[-1] - K >= 0 and curNums[-1] - K <= 9:
                curNums.append(curNums[-1] - K)
                self.DFS(curNums, N, K)
                curNums.pop(len(curNums) - 1)




print(Solution().numsSameConsecDiff(2, 0))