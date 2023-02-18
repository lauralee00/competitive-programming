import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = list(read())
        i, j = 0, n-1
        mx, mn = n, 1
        res = [-1]
        while i < j:
            if a[i] == mx:
                i += 1
                mx -= 1
            elif a[i] == mn:
                i += 1
                mn += 1
            elif a[j] == mn:
                j -= 1
                mn += 1
            elif a[j] == mx:
                j -= 1
                mx -= 1
            else:
                res = [i+1, j+1]
                break
        print(*res)




if __name__ == '__main__':
    solve()
