import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        i = 1
        b = 1
        res = [1, 0]
        while res[0] + res[1] < n:
            i += 4
            res[b] += i
            if b == 1: b = 0
            elif b == 0: b = 1
        if res[0] + res[1] == n:
            print(res[0], res[1])
        elif b == 1:
            print(n-res[1], res[1])
        elif b == 0:
            print(res[0], n-res[0])


if __name__ == '__main__':
    solve()
