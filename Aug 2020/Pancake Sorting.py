from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        n = len(A)
        for i in range(n):
            maxNum = -1
            maxPos = 0
            for j in range(n - i):
                if maxNum < A[j]:
                    maxNum = A[j]
                    maxPos = j

            if maxPos == n - i - 1:
                continue
            else:
                A = list(reversed(A[: maxPos + 1])) + A[maxPos + 1 :]
                res.append(maxPos + 1)
                A = list(reversed(A[: n - i])) + A[n - i :]
                res.append(n - i)
        return res

a = [3,2,4,1]
print(Solution().pancakeSort(a))