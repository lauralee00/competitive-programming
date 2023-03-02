import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, m = read()
        a = read()
        psum = list(accumulate(a))
        print(psum)

if __name__ == '__main__':
    solve()
