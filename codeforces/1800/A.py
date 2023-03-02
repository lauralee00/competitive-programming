import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):

        n, = read()
        s = input()
        res = []
        for c in s:
            if not res or res[-1] != c.lower():
                res.append(c.lower())

        if len(res) == 4 and res == ["m", "e", "o", "w"]:
            print('yes')
        else: print('no')

if __name__ == '__main__':
    solve()