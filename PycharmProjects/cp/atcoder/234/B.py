# https://atcoder.jp/contests/abc234/tasks/abc234_b
n = int(input())
xlist, ylist = [], []

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


for i in range(n):
    x, y = map(int, input().split())
    xlist.append((x, i))
    ylist.append((y, i))
xlist.sort(key=lambda z: z[0])
ylist.sort(key=lambda w: w[0])

for i in range(n-1, -1, -1):
    xlist[i]



new = {input().split() for _ in range(n)}


