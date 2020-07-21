from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = 0
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, A, B, i, j, index):
        if index == len(B):
            return True

        if i < 0 or i >= self.m or j < 0 or j >= self.n or B[index] != A[i][j]:
            return False

        tmp = A[i][j]
        A[i][j] = "#"

        ans = self.dfs(A, B, i + 1, j, index + 1) or \
              self.dfs(A, B, i, j + 1, index + 1) or \
              self.dfs(A, B, i - 1, j, index + 1) or \
              self.dfs(A, B, i, j - 1, index + 1)

        A[i][j] = tmp

        return ans

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

print(Solution().exist(board, word))