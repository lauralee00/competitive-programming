# https://codeforces.com/contest/1772/problem/C

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def run():
    t, = read()
    for _ in range(t):
        k, n = read()
        res = [1]
        for i in range(1, k):
            next = res[-1] + i
            # check if it's possible to fill remain
            # if remaining numbers is not enough to cover
            if n-next >= k-i-1:
                res.append(next)
            else:
                res.append(res[-1]+1)
        print(*res)

if __name__ == "__main__":
    run()
