from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n: return 0

        stock = -prices[0]
        money = 0
        pre_money = money

        for i in range(1, n):
            stock = max(stock, pre_money - prices[i])
            pre_money = money
            money = max(stock + prices[i], money)
        return money

print(Solution().maxProfit([1,2,3,0,2]))