import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        H = list(read())
        st = []
        for i, h in enumerate(H):
            if not st or h > st[-1]:
                st.append(h)
            else: # h <= st[-1], meaning array is not strictly increasing







if __name__ == '__main__':
    solve()
