# https://codeforces.com/contest/1772/problem/D

# thoughts on cases:
# 3 valid cases:

# 1. always non-decreasing:
# return first element (smallest number)

# 2. always non-increasing:
# return last element (largest number)

# 3. always non-decreasing with one contiguous non-increasing segment
# to check if valid, take the maximum length non-increasing segment
# return
import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

t, = read()
for _ in range(t):
    n, = read()
    a = list(read())
