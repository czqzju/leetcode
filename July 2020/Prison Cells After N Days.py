from copy import deepcopy
from functools import reduce

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cycle = 1
        first = [0] * 8
        for i in range(1, 7):
            first[i] = 1 if cells[i-1] == cells[i+1] else 0

        N -= 1

        cells = deepcopy(first)

        while N > 0:
            N -= 1
            temp = [0] * 8
            for i in range(1, 7):
                temp[i] = 1 if cells[i - 1] == cells[i + 1] else 0

            if reduce(lambda x, y : x and y, map(lambda p, q: p == q, temp, first), True):
                N %= cycle

            cells = deepcopy(temp)
            cycle += 1

        return cells

print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7))

