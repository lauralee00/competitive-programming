#need fixing

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

T = int(input())
for i in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    count = 0
    maxCit = C[0]
    print(f"Case #{i}:", end=" ")
    for c in C:
        if c == maxCit:
            count += 1
        elif c > maxCit:
            count = 1
        maxCit = max(maxCit, c)
        y = min(maxCit, count)
        print(f"{y}", end=" ")
