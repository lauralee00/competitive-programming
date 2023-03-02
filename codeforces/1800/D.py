import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        s = input()
        cnt = 1
        for i in range(n):
            if i >= 2 and s[i] != s[i-2]:
                cnt += 1
        print(cnt)
if __name__ == '__main__':
    solve()
