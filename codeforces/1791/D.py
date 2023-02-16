import sys
from collections import Counter, defaultdict
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        s = input()
        a = ord("a")

        completes = Counter(s)
        unique_right = len(completes)
        unique_left = 0
        max_cnt = unique_right
        cur = defaultdict(int)
        for i, c in enumerate(s):
            cur[c] += 1
            if cur[c] == 1:
                unique_left += 1
            if cur[c] == completes[c]:
                unique_right -= 1
            max_cnt = max(unique_left + unique_right, max_cnt)
        print(max_cnt)




if __name__ == '__main__':
    solve()
