import random
import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        ops = 0
        a = list(read())
        for i, elem in enumerate(a):
            if elem == 1:
                a[i] += 1
                ops += 1
            if i > 0 and a[i] % a[i-1] == 0:
                a[i] += 1
                ops += 1
        assert(ops <= 2*n)

        print(*a)

if __name__ == '__main__':
    solve()
