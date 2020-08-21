from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for num in A:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)

        return evens + odds

a = [3,1,2,4]
print(Solution().sortArrayByParity(a))