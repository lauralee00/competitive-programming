import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )
from collections import deque

def solve():
    def alternating(s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]: return False
        return True
    t, = read()
    for _ in range(t):
        n, m = read()
        s = input()
        t = input()
        sd = list(s)
        td = list(t)
        sd1 = list(s)
        td1 = list(t)
        T = False
        while sd:
            td.append(sd.pop())
            if alternating(td) and alternating(sd):
                T = True
                break
        while td1:
            sd1.append(td1.pop())
            if alternating(td1) and alternating(sd1):
                T = True
                break
        if alternating(s) and alternating(t) or T: print("Yes")
        else: print("No")

if __name__ == '__main__':
    solve()