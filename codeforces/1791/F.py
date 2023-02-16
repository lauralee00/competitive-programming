import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, q = read()
        a = list(read())
        psum = [0]*n
        for _ in range(q):
            w = read()
            if w[0] == 1:
                _, l, r = w
                psum[l] += 1
                if r+1 != n: psum[r+1] -= 1
            elif w[0] == 2:
                _, x = w
                if psum[x] >= 3:
                    print(a[x])
                else:
                    for i, val in enumerate(psum):
                        if i != n-1: psum[i+1] += psum[i]









if __name__ == '__main__':
    solve()
