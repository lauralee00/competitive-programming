# https://atcoder.jp/contests/abc235/tasks/abc235_b
# find first local maximum
n = int(input())
H = list(map(int, str(input()).split()))

prev = H[0]
for i in range(1, n):
    if H[i] <= prev:
        break
    prev = H[i]
print(prev)

