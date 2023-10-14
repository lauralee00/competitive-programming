import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        b = list(read())
        res = []
        half = 0
        full = 0
        for i, d in enumerate(b):
            if d == 1:
                # buy new
                half += 1
            elif d == 2 and half > 0:
                if half % 2 == 0: # even
                    pair =  half // 2 - 1
                    full += pair
                    half -= pair*2
                else: # odd
                    pair = half // 2
                    full += half // 2
                    half -= pair*2

            res.append(full + half)
        print(max(res))

                # examine sex


if __name__ == '__main__':
    solve()
