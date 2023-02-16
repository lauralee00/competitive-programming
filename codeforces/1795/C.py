import sys
import bisect
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read()) # amount of tea
        b = list(read()) # amount each taster can drink at once
        bccum = list(b)
        for i in range(n-1):
            bccum[i+1] += bccum[i]
        res = [0]*n
        debt = [0]*n
        # accumulation of tea
        for i in range(n):
            m = min(a[i], b[i])
            if a[i] <= b[i]: # amount of tea less than drinkable
                res[i] += 1
                if i != n-1: res[i+1] -= 1
                # print(b[i]-a[i])
                debt[i] += b[i]-a[i] # amount not drunk
            else:
                subtract = bccum[i-1] if i != 0 else 0
                idx = bisect.bisect_left(bccum, a[i]+subtract) # maximum amount of tea drinkable by everyone >= tea available
                if idx < n:
                    assert(bccum[idx] >= a[i]+subtract)
                    debt[idx] += bccum[idx]-subtract-a[i]
                    # print('bcd', bccum[idx] - a[i], debt, bccum, res)
                    res[i] += 1
                    if idx < n-1: res[idx+1] -= 1
                elif idx == n: # tea available > maximum amount of tea drinkable by everyone
                    # print(bccum, a, i, idx)
                    assert(bccum[idx-1] < a[i]+subtract)
                    # print(debt)
                    res[i] += 1

        for i in range(n-1):
            res[i+1] += res[i]
        # print("r", res)
        # print("d", debt)
        for i, x in enumerate(res):
            res[i] = b[i]*x - debt[i]
        print(*res)


if __name__ == '__main__':
    solve()
