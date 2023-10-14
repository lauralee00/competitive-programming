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
        s = input()
        res = []
        remove, swap = 0, 0
        coin = 10**12
        for i, c in enumerate(s):
            if not res or res[-1] == c:
                res.append(c)
            elif res[-1] == "0" and c == "1":

            elif res[-1] == "1" and c == "0":

            else:
                raise ValueError()

        print(coin*(remove+swap)+remove)



if __name__ == '__main__':
    solve()
