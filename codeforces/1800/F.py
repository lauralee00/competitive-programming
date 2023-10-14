# https://codeforces.com/contest/1800/problem/F
#TODO
import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
from collections import Counter, defaultdict

def solve():
    n, = read()
    words = [Counter(input()) for _ in range(n)]
    cnt = 0
    seen = defaultdict(int)
    for i in range(n):
        key = []
        for
        key.append()

            for k in range(26):
                if invalid: break
                ch = chr(ord("a")+k)
                freq = words[i][ch] + words[j][ch]
                if freq == 0:
                    if zero:
                        invalid = True
                    zero = True
                elif freq % 2 == 0:
                    invalid = True
            if not invalid: cnt += 1
    print(cnt)
if __name__ == '__main__':
    solve()
