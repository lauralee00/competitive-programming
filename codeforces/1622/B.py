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
        p = list(read())
        s = input()
        like, dislike = [], []
        for i, c in enumerate(s):
            if c == "0": # dislike
                dislike.append(i)
            elif c == "1":
                like.append(i)


if __name__ == '__main__':
    solve()
