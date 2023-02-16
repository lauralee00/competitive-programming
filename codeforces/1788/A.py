import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    n, = read()
    arr = list(read())

    for i in range(1, n):
        arr[i] *= arr[i-1]
    num = arr[-1]

    for i, e in enumerate(arr):
        if e*e == num:
            return i+1
    return -1


if __name__ == '__main__':
    t,= read()
    for _ in range(t):
        print(solve())