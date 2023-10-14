# problem: [https://codeforces.com/problemset/problem/1886/B]
# import bisect 
# from collections import defaultdict, Counter
import math
# import heapq  

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def solve():
    t, = read()
    for _ in range(t):
        px, py = read()
        ax, ay = read()
        bx, by = read()
        po, pa = distance(px, py, 0, 0), distance(px, py, ax, ay)
        pb, bo = distance(px, py, bx, by), distance(bx, by, 0, 0)
        ab, oa = distance(ax, ay, bx, by), distance(0, 0, ax, ay)
        radius = min(max(oa, pa), max(bo, pb))
        if oa <= ab/2 and pb <= ab/2:
            radius = min(radius, ab/2)
        elif pa <= ab/2 and bo <= ab/2:
            radius = min(radius, ab/2)
        if max(pb, oa)**2 >= ab:
            radius = min(radius, max(pb, oa))
        elif max(pa, bo)**2 >= ab:
            radius = min(radius, max(pa, bo))

        print(radius)

if __name__ == '__main__':
    solve()
