import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        p = [list(read()) for _ in range(n)]
        dp = [[-1, -1] for _ in range(n)]
        for i, (a, b) in enumerate(p):
            dp[i][0] = max(a, dp[i-1][0])

if __name__ == '__main__':
    solve()
