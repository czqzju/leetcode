from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        one, seven, thirty = costs
        cost = [0] * 366

        daySet = set(days)

        for i in range(1, 366):
            cost[i] = cost[i - 1]

            if len(daySet) and i in daySet:
                cost[i] = min(cost[i - 1 if i - 1 >=0 else 0] + one,
                              cost[i - 7 if i - 7 >=0 else 0] + seven,
                              cost[i - 30 if i - 30 >= 0 else 0] + thirty)
        return cost[365]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

print(Solution().mincostTickets(days, costs))
