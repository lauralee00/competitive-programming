import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, m = read()
        p = read()
        seen = set()
        removed = [-1]*n
        for i, x in enumerate(p):
            if n <= 0: break
            if x not in seen:
                # print(x, i+1, n )
                n -= 1
                removed[n] = i+1
                # print(removed)

            seen.add(x)
        print(*removed)

if __name__ == '__main__':
    solve()
