import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

#TODO:

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        i = 1
        a = 1
        cnt = 1
        res = [1, 0, 0, 0] # alice wb bob wb
        while res[0] + res[1] + res[2] + res[3] < n:
            i += 4
            cnt += 1
            if cnt % 2 == 1:
                w, b = i // 2, i - i//2
            else:
                b, w = i // 2, i - i//2
            res[a] += w
            res[a+1] += b
            if a == 2: a = 0
            elif a == 0: a = 2
        if res[0] + res[1] + res[2] + res[3] == n:
            print(res[0], res[1], res[2], res[3])
        elif a == 2:
            print(n-res[1], res[1])
        elif a == 0:
            print(res[0], n-res[0])


if __name__ == '__main__':
    solve()
