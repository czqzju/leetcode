from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for _ in range(len(prices) + 1):
            dp.append([[0, 0] for _ in range(3)])

        dp[0][1][0] = sys.maxsize
        dp[0][2][0] = sys.maxsize

        for i in range(len(prices)):
            dp[i + 1][2][1] = max(dp[i][2][1], prices[i] - dp[i][2][0])
            dp[i + 1][2][0] = min(dp[i][2][0], prices[i] - dp[i][1][1])
            dp[i + 1][1][1] = max(dp[i][1][1], prices[i] - dp[i][1][0])
            dp[i + 1][1][0] = min(dp[i][1][0], prices[i])
        return dp[len(prices)][2][1]

print(Solution().maxProfit([1,3,5,4,3,7,6,9,2,4]))