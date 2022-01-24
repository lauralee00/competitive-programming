N, Q = map(int, str(input()).split())
A = list(map(int, str(input()).split()))
seen = dict()
seen2 = dict()
Qlist = []
for i in range(Q):
    x, k = map(int, str(input()).split())
    if x not in seen:
        seen[x] = [0, set()]
    seen[x][1].add(k)
    Qlist.append((x, k))
for j in range(N):
    x = A[j]
    if x in seen:
        seen[x][0] += 1
        if seen[x][0] in seen[x][1]:
            seen[x][1].remove(seen[x][0])
            num, freq = x, seen[x][0]
            seen2[(num, freq)] = j
for z in range(Q):
    item = Qlist[z]
    if item in seen2:
        print(seen2[item] + 1)
    else:
        print(-1)
