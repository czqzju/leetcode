from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1, 1]
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        for i in range(2, rowIndex + 1):
            cur = []
            for j in range(0, i + 1):
                if j == 0:
                    cur.append(1)
                elif j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre = cur
        return pre


print(Solution().getRow(3))