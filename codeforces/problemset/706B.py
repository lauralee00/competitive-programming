# https://codeforces.com/problemset/problem/706/B

import sys
import bisect
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    n, = read()
    x = sorted(read())
    q, = read()
    for _ in range(q):
        m, = read()
        idx = bisect.bisect_right(x, m)-1
        print(idx+1)

if __name__ == '__main__':
    solve()
