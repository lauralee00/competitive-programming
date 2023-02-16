import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        s = list(input())
        i, j = 0, n-1
        while i < j:
            if s[i] == "0" and s[j] == "1" or s[i] == "1" and s[j] == "0":
                i += 1
                j -= 1
            else:
                break
        print(j-i+1)




if __name__ == '__main__':
    solve()