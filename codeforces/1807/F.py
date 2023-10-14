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
    dirs = {"DR": (1, 1), "DL": (1, -1), "UR": (-1, 1), "UL": (-1, -1)}
    for _ in range(t):
        n, m, i1, j1, i2, j2, d = input().split(" ")
        n = int(n)
        m = int(m)
        i1 = int(i1)
        i2 = int(i2)
        j1 = int(j1)
        j2 = int(j2)
        bounce = 0
        seen = [[set()]*m for _ in range(n)]
        dr, dc = dirs[d]
        while True:
            if (i1, j1) == (i2, j2):
                print(bounce)
                break
            elif 0 <= i1-1 < n and 0 <= j1-1 < m and seen[i1-1][j1-1] and (dr, dc) in seen[i1-1][j1-1]: # pattern
                print(-1)
                break
            seen[i1-1][j1-1].add((dr, dc))

            if i1 == 1 and dr == -1 or j1 == 1 and dc == -1 or i1 == n and dr == 1 or j1 == m and dc == 1: # hit wall, change direction
                bounce += 1
                # direction change
                if (i1, j1) in ((1,1), (1, m), (n, m), (n, 1)):
                    dr, dc = -dr, -dc

                elif i1 == 1 or i1 == n: # floor or top
                    dr, dc = -dr, dc

                elif j1 == 1 or j1 == m: # left or right
                    dr, dc = dr, -dc
            i1 += dr
            j1 += dc
            if not (1 <= i1 <= n and 1 <= j1 <= m):
                print(-1)
                break








if __name__ == '__main__':
    solve()
