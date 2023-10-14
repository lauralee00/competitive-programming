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
        cnts = Counter(s)
        cntt = Counter(t)
        if cnts != cntt:
            print("no")

        for i, c in enumerate(s):

            if i < k and cntt[c] == :


        else:
            print("yes")



if __name__ == '__main__':
    solve()
