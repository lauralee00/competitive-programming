import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
from collections import defaultdict

def solve():
    t, = read()
    for _ in range(t):
        n, k = read()
        s = input()
        letters = dict()
        for c in s:
            if c.lower() not in letters:
                if c == c.lower():
                    letters[c.lower()] = [1, 0]
                else:
                    letters[c.lower()] = [0, 1]
            elif c == c.lower():
                letters[c.lower()][0] += 1
            else:
                letters[c.lower()][1] += 1
        match = 0
        for c in letters:
            lower, upper = letters[c]
            match += min(lower, upper)
            swap = abs(lower-upper)//2
            if k >= swap:
                k -= swap
                match += swap
            else:
                match += k
                k = 0

        print(match)


if __name__ == '__main__':
    solve()
