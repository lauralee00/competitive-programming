import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()

    for _ in range(t):

        n, = read()
        a = list(read())
        neg = res = 0
        smallest_abs = float('inf')
        for c in a:
            smallest_abs = min(smallest_abs, abs(c))
            if c < 0:
                neg += 1
            res += abs(c)
        if neg % 2 == 0:
            print(res)
        else:
            print(res-smallest_abs*2)

# 5 
# 4
# -1 -1 -1 1
# 6
# -1 1 -1 1 1 1
# 4
# -1 1 0 1
# 4
# 0 1 -1 1
# 6
# -1 1 -1 1 -1 1
# 6
# -1 1 -1 1 -1 0



if __name__ == '__main__':
    solve()
