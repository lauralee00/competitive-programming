import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def solve(n, H):

    diffs = [0]*(n-1)

    for i in range(0, n-1):
        diffs[i] = H[i+1] - H[i]
    tot = 0
    if diffs[0] < 0: return -1
    for i, d in enumerate(diffs):
        if diffs[i] > 0 and diffs[i+1] < 0:
            if diffs[i] + diffs[i+1] >= 0:
                diffs[i] += diffs[i+1]
                tot += diffs[i+1]*4
                diffs[i+1] = 0
            else:
                return -1
        elif diffs[i] < 0 or diffs[i+1] < 0:
            return -1
    return tot

t, = read()
for _ in range(t):
    n, = read()
    H = list(map(int, input().split()))
    print(solve(n, H))
