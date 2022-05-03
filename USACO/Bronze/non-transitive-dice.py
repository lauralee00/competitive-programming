import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())
# 3
# 4 5 6 7 2 4 5 10
# 2 2 2 2 1 1 1 1
# 1 1 1 1 2 2 2 2

if __name__ == '__main__':
    t, = read()
    for _ in range(t):
        x = list(read())
        A, B = x[:4], x[4:]

        print(A, B)