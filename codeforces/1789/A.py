import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        a = sorted(list(read()))
        max_divisor = min(a)
        res = [set() for _ in range(n)]
        for idx, elem in enumerate(a):
            for i in range(1, min(elem, max_divisor)+1):
                if elem % i == 0:
                    res[idx].add(i)
        print(res)
        it = set()
        beautiful = True
        for i in range(n):
            if not beautiful: break
            if i == 0: it = res[i]
            else: it = it.intersection(res[i])

            if i > 0:
                for elem in it:
                    if elem > i+1:
                        print(i, it, elem)
                        beautiful = False
                        break

        if not beautiful:
            print("no")
        else:
            print("yes")



if __name__ == '__main__':
    solve()