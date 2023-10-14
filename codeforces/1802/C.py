import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())



def solve():
    t, = read()

    for _ in range(t):
        n, m = read()
        seen = set()
        res = [[0] * m for _ in range(n)]

        carry = 1
        tl, tr, bl, br = 8, 9, 10, 11
        for i in range(n):
            for j in range(m):
                if i % 2 == 0 and j % 2 == 0:
                    if tl not in seen:
                        res[i][j] = tl
                    else:
                        carry *= 2
                        res[i][j] += carry
                elif i % 2 == 0 and j % 2 == 1:
                    if tr not in seen:
                        res[i][j] = tr
                elif i % 2 == 1 and j % 2 == 0:
                    if bl not in seen:
                        res[i][j] == bl
                elif i % 2 == 1 and j % 2 == 1:
                    if br not in seen:
                        res[i][j] == br
                seen.add(res[i][j])

if __name__ == '__main__':
    solve()
