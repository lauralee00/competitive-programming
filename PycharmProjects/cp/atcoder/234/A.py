def f(x):
    return x**2+2*x+3
t = int(input())
res = f(t)
res2 = f(res+t)
res3 = f(res)
print(f(res2+res3))