import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, c = read()
        a = list(read())
        a.sort()

        cnt += 1
        # print(res)
        print(cnt)

if __name__ == '__main__':
    solve()
