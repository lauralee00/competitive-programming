# problem: [link]
# import bisect 
# from collections import defaultdict, Counter
# import math
# import heapq  
import random
import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        # parity check for size 2
        # odd even odd even odd even odd
        res = list(range(1, n+1))
        if len(res) <= 2:
            print(*res)
            continue

        cant = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (i+1 + j+1 + k+1) % 3 == 0:
                        cant.add((i+1, j+1, k+1))


        invalid = True
        cnt = 0
        while cnt < 10**4 and invalid:
            random.shuffle(res)
            for i in range(len(res)-2):
                if sum(res[i:i+3]) % 3 == 0:
                    invalid = True
                    break
                else:
                    invalid = False
            cnt += 1
        if not invalid:
            print(*res)
        else:
            print(-1)




if __name__ == '__main__':
    solve()
