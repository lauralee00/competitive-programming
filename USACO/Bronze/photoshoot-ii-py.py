import sys

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = maxSum = 0

for (a, b) in zip(A, B):
    sum += a & b

