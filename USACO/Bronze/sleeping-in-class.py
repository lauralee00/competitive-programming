T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    res = []
    maxNum = max(A)
    if maxNum == 0:
        print(0)
        continue
    curSum = 0

    targets = [i for i in range(maxNum, sumA+1) if sumA % i == 0]
    for target in targets:
        curSum = target
        op = 0
        for i, n in enumerate(A):
            if n == curSum:
                curSum = target
                continue
            elif n < curSum:
                curSum -= n
                op += 1
                continue
            else: break
        if i == len(A) - 1:
            break
    print(op)






