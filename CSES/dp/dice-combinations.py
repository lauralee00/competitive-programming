import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

# https://cses.fi/problemset/task/1633/

n = int(input())
dp = [1] + [0]*n
mod = 10**9 + 7
for i in range(n+1):
    for j in range(1, 7):
        if i-j >= 0:
            dp[i] += dp[i-j] % mod
            dp[i] %= mod
print(dp[-1] % mod)


