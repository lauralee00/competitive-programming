import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
import heapq

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        s = list(read())
        hero_cnt = s.count(0)
        bonus = []
        res = 0
        for c in s:
            if c > 0:
                heapq.heappush(bonus, -c)
            else:
                if bonus:
                    val = -heapq.heappop(bonus)
                    res += val
        print(res)

if __name__ == '__main__':
    solve()
