import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        nums = [0]*(2*n+1)
        if n % 2 == 0:
            print("No")
            continue
        s1 = 1 + 2 * n - (n - 1) // 2
        sn = s1+n-1
        res = []

        print(s1, sn)
        for i in reversed(range(s1, sn+1)):
            big = min(2*n, i-1)
            small = i-big
            while small < big and nums[small] or nums[big]:
                if not 0 < small <= 2 * n and 0 < big <= 2 * n: raise ValueError
                print(small, big)
                small += 1
                big -= 1
                if small == big:
                    small += 1
                    big -= 1
            if not 0 < small < 2*n and 0 < big <= 2*n:
                print("error")
            else:
                nums[small] = 1
                nums[big] = 1
                res.extend([small, big])
        print(res[::-1])








if __name__ == '__main__':
    solve()
