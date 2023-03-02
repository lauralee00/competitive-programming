import sys
import bisect
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    mod = 998244353
    two = three = 1
    twos = [1]
    threes = [1]
    while two <= 10**6:
        two *= 2
        two %= mod
        twos.append(two)
    while three <= 10**6:
        three *= 3
        three %= mod
        threes.append(three)

    for _ in range(t):
        l, r = read()
        mx = 0
        cnt = 0
        two_idx = bisect.bisect_right(twos, r//l)
        three_idx = bisect.bisect_right(threes, r//l)
        while l < r:
            mult = r//l
            if mult >= twos[two_idx-1]:
                cnt += 1
            else:
                break
            if mult >= threEs[three_idx-1]:
                mx = three_idx
                cnt += 1
            cnt %= mod

            l += 1
        print(mx, cnt%mod)

if __name__ == '__main__':
    solve()
