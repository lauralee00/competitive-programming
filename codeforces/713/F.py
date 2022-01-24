# https://codeforces.com/contest/1512/problem/F

import sys
input = lambda: sys.stdin.readline().strip()
read  = lambda: map( int,  input().split() )


def solve(n, c):
    pass


if __name__ == '__main__':
    t, = read()
    for _ in range(t):
        n, c = read()
        print(solve(n, c))
