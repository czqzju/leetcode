class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        pre1 = 2
        pre2 = 1
        res = 0

        for i in range(3, n + 1):
            res = pre1 + pre2
            pre2 = pre1
            pre1 = res
        return res

print(Solution().climbStairs(4))



