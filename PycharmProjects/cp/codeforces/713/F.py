import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

# https://codeforces.com/contest/1512/problem/F

def solve(n, c):


if __name__ == '__main__':
    t, = read()
    for _ in range(t):
        n, c = read()
        print(solve(n, c))
