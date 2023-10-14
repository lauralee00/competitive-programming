# problem: [https://codeforces.com/problemset/problem/1886/B]
# import bisect 
# from collections import defaultdict, Counter
import math
# import heapq  

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def in_circle(cirx, ciry, px, py, radius):
    return (cirx-px)**2 + (ciry-py)**2 <= radius**2

def solve():
    t, = read()
    for _ in range(t):
        px, py = read()
        ax, ay = read()
        bx, by = read()
        lo, hi = 0, 10**6
        while abs(hi-lo) > 10**(-6):
            w = (lo+hi)/2
            if in_circle(ax, ay, px, py, w) and in_circle(ax, ay, 0, 0, w):
                hi = w
            elif in_circle(bx, by, px, py, w) and in_circle(bx, by, 0, 0, w):
                # reduce w
                hi = w
            elif (ax-bx)**2 + (ay-by)**2 <= (2*w)**2: # intersects
                if in_circle(ax, ay, px, py, w) and in_circle(bx, by, 0, 0, w):
                    hi = w
                elif in_circle(ax, ay, 0, 0, w) and in_circle(bx, by, px, py, w):
                    hi = w
                else: lo = w
            else: # can't get there
                lo = w
        print(lo)




'''
-4 0
5 -3
-4 3
0 2
1 5
-2 5
-1 1
-1 5
-4 -1
3 2
1 3
0 -1
5 -3
-3 1
-3 -3
-3 1
1 5
-4 -5
1 3
-3 3
'''
if __name__ == '__main__':
    solve()
