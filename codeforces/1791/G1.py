import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, c = read()
        a = list(read())
        cnt = _sum = 0
        res = [0]*n
        for i in range(n):
            res[i] += i + 1 + a[i]
        res.sort()
        for num in res:
            _sum += num
            if _sum > c:
                break
            cnt += 1
        # print(res)
        print(cnt)

if __name__ == '__main__':
    solve()
