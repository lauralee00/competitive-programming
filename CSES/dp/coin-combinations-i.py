import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

# https://cses.fi/problemset/task/1635

n, x = read()
c = list(read())

mod = 10**9 + 7

dp = [1] + [0]*x
for i in range(1, x+1):
    for coin in c:
        if i - coin >= 0:
            dp[i] += dp[i-coin] % mod
            dp[i] %= mod
print(dp[-1] % mod)
