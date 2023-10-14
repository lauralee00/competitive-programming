# problem: [link]
# import bisect 
from collections import defaultdict, Counter
# import math
# import heapq  

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        c = list(read())
        # cnts = Counter(c)
        c.sort()
        tot = 1
        res = "yes"
        for i, num in enumerate(c):
            if num > tot:
                res = "no"
                break
            if i == 0:
                tot -= 1
            tot += num
        print(res)
if __name__ == '__main__':
    solve()
