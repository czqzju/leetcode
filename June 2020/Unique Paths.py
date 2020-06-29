class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        small = min(m-1, n-1)
        a = 1
        b = 1
        for i in range(m - 1 + n - 1, m - 1 + n - 1 - small, -1):
            a *= i
        for i in range(1, small + 1):
            b *= i
        return a // b

print(Solution().uniquePaths(7, 3))