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
        n, = read()
        a = list(read())
        b = list(read())
        for i, j in zip(a,b):
            if i < j and i 

if __name__ == '__main__':
    solve()