N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [0] + [float('inf')]*(N-1)

for i in range(1, N):
    for j in range(1, min(i, K) + 1):
        dp[i] = min(dp[i], dp[i-j]+abs(H[i]-H[i-j]))
print(dp[-1])


