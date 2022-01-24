# https://codeforces.com/contest/1624/problem/B
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    # case 1: a*m, b, c is an arithmetic progression
    # d = c-b then a*m = b-d -> m = (b-d)//a
    if (2*b-c) and (2*b-c) % a == 0:
        print("Yes")
    # case 2: a, b*m, c is an arithmetic progression
    # d = (c-a)//2 a+d = b*m -> m == a+d//b
    elif (c-a) % 2 and (c-a) // 2 and (a + (c - a) // 2) and (a + (c - a) // 2) % b == 0:
        print("Yes")
    # case 3: a, b, c*m is an arithmetic progression:
    # d = b-a and 2b-a = c*m -> m == (2b-a)//c
    elif (2*b-a) and (2*b-a) % c == 0:
        print("Yes")
    else:
        print('No')
