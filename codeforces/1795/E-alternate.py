import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
#TODO

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        H = list(read())
        prev = None
        basic = 0
        for i, h in enumerate(H):
            if i > 0 and H[i-1] >= h:
                basic += H[i-1]-h+1
                H[i-1] = h-1






if __name__ == '__main__':
    solve()
