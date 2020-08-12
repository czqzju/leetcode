from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.freshCnt = 0
        self.minTime = 0
        self.curRottenOrgs = []
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    self.freshCnt += 1
                elif grid[i][j] == 2:
                    self.curRottenOrgs.append((i, j))
        while self.freshCnt and len(self.curRottenOrgs):
            self.minTime += 1
            self.nextRottens = []
            for i, j in self.curRottenOrgs:
                grid[i][j] = 0
                rottenOut = self.updateAdj(i, j, grid)
                if rottenOut:
                    return self.minTime
            self.curRottenOrgs = self.nextRottens

        if self.freshCnt:
            return -1
        else:
            return self.minTime

    def updateAdj(self, i: int, j: int, grid: List[List[int]])->bool:
        if self.checkPosValid(i - 1, j):
            rottenOut = self.updateOrg(i - 1, j, grid)
            if rottenOut:
                return True
        if self.checkPosValid(i + 1, j):
            rottenOut = self.updateOrg(i + 1, j, grid)
            if rottenOut:
                return True
        if self.checkPosValid(i, j - 1):
            rottenOut = self.updateOrg(i, j - 1, grid)
            if rottenOut:
                return True
        if self.checkPosValid(i, j + 1):
            rottenOut = self.updateOrg(i, j + 1, grid)
            if rottenOut:
                return True
        return False

    def checkPosValid(self, i: int, j: int)-> bool:
        if i >= 0 and i < self.rows and j >= 0 and j < self.cols:
            return True
        else:
            return False

    def updateOrg(self, i: int, j: int, grid: List[List[int]])->bool:
        if grid[i][j] == 1:
            grid[i][j] = 2
            self.nextRottens.append((i, j))
            self.freshCnt -= 1
            if self.freshCnt <= 0:
                return True
        else:
            return False

sdfsdgdsfgs



print(Solution().orangesRotting([[0,2]]))