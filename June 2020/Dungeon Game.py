import sys
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = len(dungeon[0]) if(row) else 0

        dp = [[sys.maxsize] * (col + 1) for i in range(row + 1)]
        dp[row - 1][col] = 1
        dp[row][col - 1] = 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0]


a = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(Solution().calculateMinimumHP(a))

