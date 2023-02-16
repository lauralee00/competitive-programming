import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    N, = read()
    S = input()
    qcnt = 0
    res = []
    for i, s in enumerate(S):
        if s == '"': # or "`""
            qcnt += 1
            res.append(s)
        elif s == ',':
            if qcnt % 2 == 0: # enclosed ,
                res.append(".") # change to .
            else:
                res.append(",")
        else:
            res.append(s)
    return res

if __name__ == "__main__":
    print("".join(solve()))

