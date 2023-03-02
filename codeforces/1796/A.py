import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    string = "FBFFBFFBFBFFBFFBFBFFBFFB"
    for _ in range(t):
        k, = read()
        s = input()
        if s in string:
            print("yes")
        else:
            print("no")




if __name__ == '__main__':
    solve()