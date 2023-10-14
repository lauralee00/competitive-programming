import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )
from collections import defaultdict

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(map(str, input().split()))
        res = []
        yes = "no"
        for w in a:
            # print(w)
            if len(w) == n-1 and res and "".join(w[::-1]) in res:
                yes = "yes"
                break
            res.append(w)
        print(yes)


if __name__ == '__main__':
    solve()