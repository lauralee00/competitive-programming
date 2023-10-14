import math
import sys
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

#TODO

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read())
        # compute maximum score for every index
        score = 1
        res = [1]*n
        start = 0
        score, d = 1, 0
        for i, s in enumerate(a):
            d += 1
            if s >= d:
                score *= s/d
            else:
                score *= s/a[start]
                start += 1
                d -= 1
                while d/a[start] > 1:
                    score *= d/a[start]
                    start += 1
                    d -= 1
        res[i] = d
        print(*res)

        print(res)
if __name__ == '__main__':
    solve()
