import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

# https://cses.fi/problemset/task/1634

n, x = read()
c = list(read())
dp = [0] + [float('inf')]*x

for i in range(x+1):
    for coin in c:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)
print(dp[-1] if dp[-1] != float('inf') else -1)