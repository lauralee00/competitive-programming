# problem: [link]
# import bisect 
# from collections import defaultdict, Counter
# import math
import heapq

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = sorted(read())
        if 0 in a:
            cnt = a.count(0)
            if 2*cnt-1 <= n:
                print(0)
                continue
            else:
                if n - a.count(0) - a.count(1) == 1:
                    val = 0
                    for c in set(a):
                        if c != 0 and c != 1:
                            val = c
                            break

                # if the 2nd biggest number is not 1 return 1 else return 2 or whatever
                if a[-1] == 1 or a[-2] == 1:
                    print(2 if a[-1] != 2 else 3)
                    continue
                else:
                    print(1)
                    continue



        else:
            print(0)
            continue

if __name__ == '__main__':
    solve()
