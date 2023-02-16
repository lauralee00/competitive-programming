import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        strn = str(n)
        arr = [[0,0] for _ in range(len(strn))]
        for i, digit in enumerate(strn):
            digit = int(digit)
            small = digit//2
            big = digit - small
            arr[i] = [small, big]

        x, y = 0, 0
        x_dsum, y_dsum = 0, 0
        for small, big in arr:
            x *= 10
            y *= 10
            if x_dsum < y_dsum:
                x += big
                y += small
                x_dsum += big
                y_dsum += small
            else:
                x += small
                y += big
                x_dsum += small
                y_dsum += big
        print(x, y)





if __name__ == '__main__':
    solve()
