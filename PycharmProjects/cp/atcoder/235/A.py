n = int(input())
tot = 0
for i in range(3):
  tot += n
  n = (n % 10)*100 + n // 10
print(tot)


