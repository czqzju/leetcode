class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].insert(len(grid[i]), 0)
        grid.insert(0, [0] * len(grid[0]))
        grid.insert(len(grid), [0] * len(grid[0]))

        perimeter = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1:
                    perimeter += self.getCellEdges(i, j, grid)

        return perimeter

    def getCellEdges(self, i, j, grid):
        edges = 0
        if grid[i - 1][j] == 0:
            edges += 1
        if grid[i][j - 1] == 0:
            edges += 1
        if grid[i][j + 1] == 0:
            edges += 1
        if grid[i + 1][j] == 0:
            edges += 1
        return edges


print(Solution().islandPerimeter([[0,1,0,0],
                            [1,1,1,0],
                            [0,1,0,0],
                            [1,1,0,0]]))
