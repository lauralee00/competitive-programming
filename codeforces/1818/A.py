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
        n, k = read()
        ops = [list(input()) for _ in range(n)]
        valid = [True]*n
        for i in range(k):
            stance = ops[0][i]
            for j in range(n):
                if ops[j][i] != stance:
                    valid[j] = False
        print(valid.count(True))



if __name__ == '__main__':
    solve()