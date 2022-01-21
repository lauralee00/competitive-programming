import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def check(row, col, index, visited):

            if index == len(word):
                return True

            if not valid(row, col) or \
                    word[index] != board[row][col] or \
                    visited[row][col]:
                return False
            visited[row][col] = 1

            res = check(row - 1, col, index + 1, visited) or \
                  check(row + 1, col, index + 1, visited) or \
                  check(row, col - 1, index + 1, visited) or \
                  check(row, col + 1, index + 1, visited)

            visited[row][col] = 0
            return res

        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if check(i, j, 0, visited): return True
        return False
