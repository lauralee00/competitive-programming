# problem: [https://codeforces.com/contest/1622/problem/C]
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
        n, k = read()
        a = list(read())
        a.sort()
        tot = sum(a)
        ok = 0
        for c in a:
            if c <= k:
                ok += 1
        if a[0] <= k:
            print(n-ok)
        else:
            print(n-1+a[0]-k)

if __name__ == '__main__':
    solve()
