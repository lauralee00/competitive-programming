import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        s = input()
        r, c = 0, 0
        for w in s:
            res = "no"
            if w == "L":
                c -= 1
            elif w == "R":
                c += 1
            elif w == "U":
                r += 1
            elif w == "D":
                r -= 1

            if (r, c) == (1, 1):
                res = "yes"
                break
        print(res)
if __name__ == '__main__':
    solve()