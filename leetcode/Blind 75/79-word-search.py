import sys
from typing import List

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

# Time Complexity : O ( m * n * 3^k ) -> k = len(word)
# Space Complexity: O (     1       ) -> board doesn't count

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def check(row, col, index):

            if index == len(word):
                return True

            if not valid(row, col) or \
                    word[index] != board[row][col] or \
                    not board[row][col]:
                return False

            # mark visited on board, save board value as char
            char, board[row][col] = board[row][col], None

            res = check(row - 1, col, index + 1) or \
                  check(row + 1, col, index + 1) or \
                  check(row, col - 1, index + 1) or \
                  check(row, col + 1, index + 1)

            board[row][col] = char # backtracking
            return res

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if check(i, j, 0): return True
        return False
