import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


# x is to be chosen, a is given
def f(x, a):
    return x // a + x % a

t, = read()
for _ in range(t):
    l, r, a = read()  # a in [l, r] are inclusive
    lim = r-a
    maxV = -1
    tog = False
    while r > lim and r >= l:
        maxV = max(maxV, f(r, a))
        if r % a == 0:
            print(f(r-1, a))
            tog = True
            break
        r -= 1
    if not tog: print(maxV)



