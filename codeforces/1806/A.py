# problem: [link]
# import bisect 
# from collections import defaultdict, Counter
# import math
# import heapq  

import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        a, b, c, d = read()
        if b > d:
            print(-1)
            continue
        if a+d-b < c:
            print(-1)
            continue
        print(a+2*(d-b)-c)

if __name__ == '__main__':
    solve()