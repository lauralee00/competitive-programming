import sys
import math
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        _, = read()
        arr = list(read())
        sum_arr = sum(arr)
        rs = 0
        max_gcd = 1
        for i, num in enumerate(arr):
            rs += num
            if i != len(arr)-1:
                max_gcd = max(max_gcd, math.gcd(rs, sum_arr-rs))
        print(max_gcd)


if __name__ == '__main__':
    solve()
