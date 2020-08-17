from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        index = 0
        res = [0] * num_people
        while candies > 0:
            allocated = min(candies, index + 1)
            candies -= allocated
            res[index % num_people] += allocated
            index += 1

        return res


print(Solution().distributeCandies(10, 3))