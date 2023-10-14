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
        n, = read()
        a = list(read())
        mihai, bianca = 0, 0

        for c in a:
            if c % 2 == 0:
                mihai += c
            else:
                bianca += c
        if mihai > bianca:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    solve()
