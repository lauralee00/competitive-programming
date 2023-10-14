# TODO problem: [https://codeforces.com/problemset/problem/1738/B]
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
        s = list(read())
        arr = []
        for i in range(n-1):
            arr.append(s[i+1]-s[i])
        if s[0]



if __name__ == '__main__':
    solve()
