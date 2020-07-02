class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        level = 0
        row = 1
        if (n == 0): return 0
        else:
            while (n >= row):
                n -= row
                row += 1
                level += 1
        return level

print(Solution().arrangeCoins(1804289383))