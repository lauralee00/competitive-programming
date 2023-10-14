import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )
from collections import defaultdict
def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read())
        a.sort(reverse=True)
        cnt = 0
        dct = defaultdict(int)
        res = []
        pos = neg = 0
        for i, b in enumerate(a):
            if b > 0:
                cnt += 1
                dct[b] += 1
                pos += 1
            else:
                cnt -= 1
                dct[b] += 1
                neg += 1
            res.append(cnt)
        print(*res)
        res = []
        cnt = 0
        seen = set()
        while pos or neg:
            if not res or res[-1] == 0:
                pos -= 1
                res.append(1)
            elif res[-1] > 0:
                if neg:
                    res.append(res[-1]-1)
                    neg -= 1
                elif pos:
                    res.append(res[-1]+1)
                    pos -= 1
        print(*res)

if __name__ == '__main__':
    solve()