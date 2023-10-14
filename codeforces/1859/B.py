# problem: [https://codeforces.com/problemset/problem/1859/B]
# import bisect 
# from collections import defaultdict, Counter
# import math
import heapq

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        res = []
        tot = 0
        for _ in range(n):
            m, = read()
            res.append(sorted(read())[:2])
        if n == 1:
            print(res[0][0])
            continue
        res.sort(key=lambda x: x[1])
        mn = res[0][0]
        for i in range(1, len(res)):
            x1, x2 = res[i]
            tot += x2
            mn = min(mn, x1)
        tot += mn
        print(tot)


if __name__ == '__main__':
    solve()
