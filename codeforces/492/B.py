import sys
import math
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
epsilon = 10**(-9)

#TODO

def solve():
    n, l = read()
    a = read()
    a = set(a)
    lo, hi = 0, l
    while abs(hi-lo) > epsilon:
        mid = (lo + hi) / 2
        print(lo, hi)
        road = [0] * (l + 1)
        for lantern in a:
            left = max(0, math.ceil(lantern-mid))
            right = min(l, math.floor(lantern+mid))
            print(left, right, lantern, mid, l)
            if right != l:
                print("right", right, lantern)
                road[right+1] -= 1
                print(road)
            road[left] += 1
        print(mid, road)
        cover = True
        for i, r in enumerate(road):
            if i != len(road)-1:
                road[i+1] += r
        print(mid, road)
        for r in road:
            if not r:
                cover = False
                break
        if cover:
            hi = mid
        else:
            lo = mid
    print(lo)


if __name__ == '__main__':
    solve()
