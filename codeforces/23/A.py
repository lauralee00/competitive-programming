import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

t, = read()
for _ in range(t):
    s  = input()
    c = input()
    lens = len(s)
    tog = False
    if s == c:
        print("YES")
        continue

    for i, w in enumerate(s):
        if w == c and (i != 0 and i != lens and i % 2 == 0):
            print("YES")
            tog = True
            break
    if not tog: print("NO")