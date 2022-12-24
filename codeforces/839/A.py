# https://codeforces.com/contest/1772/problem/A

import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

t, = read()
for _ in range(t):
    a, b = map(int, input().split("+"))
    print(a+b)

