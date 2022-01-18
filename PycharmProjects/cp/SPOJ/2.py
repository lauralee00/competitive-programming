# https://www.spoj.com/problems/PRIME1/
# TLE
def is_prime(m, seenPrimes, seenNotPrimes):
    if m in seenPrimes: return True
    elif m in seenNotPrimes: return False
    sqrt_m = int(m**(1/2))
    for i in range(2, sqrt_m+1):
        if m % sqrt_m == 0:
            seenNotPrimes.add(m)
            return False
    seenPrimes.add(m)
    return True


seenPrimes = set()
seenNotPrimes = set()
t = int(input())
for _ in range(t):
    m, n = map(int, str(input()).split())
    while m <= n:
        if is_prime(m, seenPrimes, seenNotPrimes): print(m)
        m += 1
    print("\n")

