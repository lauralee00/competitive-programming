import sys
input = lambda : sys.stdin.readline().strip()
read  = lambda : map( int,  input().split() )

v, a, b, c = read()
arr = {'F': a; 'M': b, 'T': c}

for w in arr:
    v -= arr[w]
    if v < 0:
        print(w)
        break