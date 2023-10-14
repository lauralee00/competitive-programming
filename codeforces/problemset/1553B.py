# TODO: [https://codeforces.com/problemset/problem/1553/B]
# import bisect 
from collections import defaultdict, Counter, deque
# import math
# import heapq  

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    q, = read()
    for _ in range(q):
        s = input()
        t = input() # target
        que = deque()
        for i, c in enumerate(s):
            if c == t[0]:
                q.append((c, i))
        strlen = 0
        while que:
            if strlen > len(s):
                print("no")
                break
            for _ in range(len(que)):
                w, idxs = que.popleft()
            strlen += 1


if __name__ == '__main__':
    solve()
