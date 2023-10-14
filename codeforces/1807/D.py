# problem: [link]
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
        n, q = read()
        a = list(read())
        for i, c in enumerate(a):
            if i != 0:
                a[i] += a[i-1]
        for _ in range(q):
            #queries
            l, r, k = read()
            l -= 1
            r -= 1
            total = a[-1]
            replace = a[r]-(a[l-1] if l != 0 else 0)
            val = total - replace + k*(r-l+1)
            if val % 2 == 1:
                print("yes")
            else:
                print("no")
if __name__ == '__main__':
    solve()
