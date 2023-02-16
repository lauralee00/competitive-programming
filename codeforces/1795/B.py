import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, k = read()
        res = [0]*51
        for i in range(n):
            l, r = read()
            if l <= k <= r:
                res[l] += 1
                if r != 50: res[r+1] -= 1

        for i in range(len(res)-1):
            res[i+1] += res[i]
        mx = max(res)
        if mx == res[k] and res.count(mx) == 1: print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    solve()
