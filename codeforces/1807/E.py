# problem: [link]
# import bisect 
# from collections import defaultdict, Counter
# import math
# import heapq

import sys
import copy

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read())
        combined_stone_cnt = copy.deepcopy(a)
        for i, c in enumerate(combined_stone_cnt):
            if i != 0:
                combined_stone_cnt[i] += combined_stone_cnt[i-1]
        lo, hi = 0, n
        while lo < hi:
            mid = (lo+hi)//2

            print(f"? {mid+1}", end=" ")
            print(*range(1, mid+2))
            sys.stdout.flush()

            weight, = read()
            if weight != combined_stone_cnt[mid]: # weight 2 is previous idx
                hi = mid
            else:
                lo = mid + 1
        print(f"! {lo+1}")
        sys.stdout.flush()
if __name__ == '__main__':
    solve()
