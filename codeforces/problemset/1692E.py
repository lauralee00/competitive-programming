# TODO problem: [https://codeforces.com/problemset/problem/1692/E]
# import bisect 
# from collections import defaultdict, Counter
# import math
# import heapq  

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, s = read()
        a = list(read())
        tot = sum(a)
        if tot < s:
            print(-1)
            continue
        l, r = 0, n-1
        one_ops = 0
        zero_ops = 0
        while r >= 0 and tot != s:
            if a[r] == 1:
                a.pop()
                r -= 1
                tot -= 1
        if tot == s: print()

if __name__ == '__main__':
    solve()
