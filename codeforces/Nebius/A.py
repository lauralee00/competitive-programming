import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        a, b = read()
        x = None # a was moved
        res = 0
        while a != 0 and b != 0:

            if x != "a":
                if a != 0:
                    if a > 0: a -= 1
                    else: a += 1
                    x = "a"
                    res += 1
                elif a == 0:
                    b -= 1
                    x = "b"
                    res += 2
            elif x == "a":
                if b != 0:
                    if b > 0: b -= 1
                    elif b < 0: b += 1
                    x = "b"
                    b -= 1
                    res += 1
                elif b == 0:
                    x = "a"
                    if a > 0: a -= 1
                    elif a < 0: a += 1
                    res += 2
        print(res)


        print(res)
if __name__ == '__main__':
    solve()