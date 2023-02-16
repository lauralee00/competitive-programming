import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        c = input()
        if c in "codeforces":
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()