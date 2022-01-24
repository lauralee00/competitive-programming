# https://codeforces.com/contest/1624/problem/A

t = int(input())
for _ in range(t):
    x = input() # trash input for n
    arr = list(map(int, input().split()))
    print(max(arr) - min(arr))