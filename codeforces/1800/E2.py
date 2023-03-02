# TODO

import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
from collections import Counter, deque

def solve():
    for _ in range(int(input())):
        n, k = read()
        s = input()
        t = input()
        q = deque()
        can = True
        if Counter(s) is not Counter(t):
            print("no")
            continue
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            idx, (a, b) = q.popleft()
            if i-idx > k:
                can = False
                break
            elif i-idx == k or i-idx == k+1 and a == t[i] and b == s[i]:
            else:
                q.append((idx, (a, b)))

        if can:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    solve()
