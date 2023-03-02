import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

#TODO: incomplete

def solve():
    t, = read()
    for _ in range(t):
        ab = [0, 0]
        a1, a2, a3, a4 = read()
        if not a1:
            print(1)
            continue
        ab[0] += a1
        ab[1] += a1
        res = a1
        negate = min(a2, a3)
        res += negate*2
        a2 -= negate
        a3 -= negate
        if min(ab) >= a2:
            res += a2
            ab[1] -= a2
        else:
            res += min(ab) + 1
            print(res)
            continue
        if min(ab) >= a3:
            res += a3
            ab[0] -= a3
        else:
            res += min(ab) + 1
            print(res)
            continue
        if min(ab) >= a4:
            res += a4
            print(res)
            continue
        else:
            res += min(ab) + 1
            print(res)
            continue

if __name__ == '__main__':
    solve()
