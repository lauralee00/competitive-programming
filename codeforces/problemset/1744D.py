# https://codeforces.com/problemset/problem/1744/D

import sys
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def solve():
    t, = read()
    power2 = []
    for _ in range(t):
        n, = read()
        a = read()
        cnt = 0
        res = []
        for i, x in enumerate(a):
            while x % 2 == 0: # log(x)
                cnt += 1
                x //= 2
            one_idx = i + 1

            twos = 0
            while one_idx % 2 == 0:
                twos += 1
                one_idx //= 2
            res.append(twos)
        res.sort()
        rpnt = n-1
        cnt2 = 0
        while rpnt >= 0 and cnt < n:
            cnt += res[rpnt]
            rpnt -= 1
            cnt2 += 1
        if rpnt == -1 and cnt < n:
            print(-1)
        else:
            print(cnt2)


if __name__ == '__main__':
    solve()
