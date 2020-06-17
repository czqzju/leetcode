class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = 0
        if (row != 0):
            col = len(board[0])
        for i in [0, row - 1]:
            for j in range(col):
                if (board[i][j] == "O"):
                    board[i][j] = "$"
                    self.DFS(i, j, board, row, col)
        for i in [0, col - 1]:
            for j in range(1, row - 1):
                if (board[j][i] == "O"):
                    board[j][i] = "$"
                    self.DFS(j, i, board, row, col)

        for i in range(row):
            for j in range(col):
                if (board[i][j] == "O"):
                    board[i][j] = "X"
                elif (board[i][j] == "$"):
                    board[i][j] = "O"

    def DFS(self, i, j, board, row, col):
        if (self.CheckIndex(i - 1, j, row, col)):
            if (board[i - 1][j] == "O"):
                board[i - 1][j] = "$"
                self.DFS(i - 1, j, board, row, col)
        if (self.CheckIndex(i + 1, j, row, col)):
            if (board[i + 1][j] == "O"):
                board[i + 1][j] = "$"
                self.DFS(i + 1, j, board, row, col)
        if (self.CheckIndex(i, j - 1, row, col)):
            if (board[i][j - 1] == "O"):
                board[i][j - 1] = "$"
                self.DFS(i, j - 1, board, row, col)
        if (self.CheckIndex(i, j + 1, row, col)):
            if (board[i][j + 1] == "O"):
                board[i][j + 1] = "$"
                self.DFS(i, j + 1, board, row, col)

    def CheckIndex(self, i, j, row, col):
        if (i < 0 or i >= row or j < 0 or j >= col):
            return False
        else:
            return True
