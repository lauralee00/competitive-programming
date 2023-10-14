# problem: [link]
# import bisect 
from collections import defaultdict, Counter
# import math
# import heapq  

import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        s = input()
        cnts = Counter(s)
        vals = list(set(list(cnts.values())))
        if len(vals) == 1:
            print("yes")
        elif len(vals) == 2 and abs(vals[0]-vals[1]) == 1:
            print("yes")
        else:
            print("no")
if __name__ == '__main__':
    solve()