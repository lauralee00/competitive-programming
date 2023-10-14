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
        s = input()
        dct = defaultdict(set)
        res = "yes"
        for i, c in enumerate(s):
            dct[c].add(i)
        for c in dct:
            odd, even = 0, 0
            for idx in dct[c]:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if odd and even:
                res = "no"
                break

        print(res)
if __name__ == '__main__':
    solve()
