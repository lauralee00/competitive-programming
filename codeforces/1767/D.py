import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    n, = read()
    s = input()
    arr = [True]*(2**n)
    i, j = 0, len(arr)-1
    for c in s:
        if c == "0": # lower
            arr[j] = False 
            j -= 1 
        if c == "1": # higher
            arr[i] = False 
            i += 1 
    for i, c in enumerate(arr):
        if c: print(i+1, end=" ")
            




if __name__ == '__main__':
    solve()
