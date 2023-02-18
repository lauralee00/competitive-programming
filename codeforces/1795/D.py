import sys
from math import factorial

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    n, = read()
    w = list(read())
    mod = 998244353
    res = 1
    read()
    for i in range(0, n, 3):
        three = [w[i], w[i+1], w[i+2]]
        three.sort()
        w1, w2, w3 = three
        # 3 cases:
        # 1. all distinct values -> choose biggest 2 -> 1 case
        # 2. two are same, one is bigger -> must choose one, one of two -> 2 cases
        # 3. two are same, one is smaller -> must choose two -> 1 case
        # 4. all same -> choose any -> 3C2 -> 3 cases

        if w1 != w2 != w3:
            pass
        elif w1 == w2 and w2 != w3:
            res = (res * 2) % mod
        elif w2 == w3 and w1 != w2:
            pass
        else:
            res = (res * 3) % mod
    res %= mod
    k = n // 3
    res = (res * (factorial(k)//(factorial(k//2))**2)) % mod

    print(res % mod)


if __name__ == '__main__':
    solve()
