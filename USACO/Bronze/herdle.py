# puzzle 3x3 grid
# each grid occupied
# 26 breeds (A~Z)
# green in grid -> correct
# yellow --> incorrect
import sys
from collections import defaultdict, Counter
read  = lambda: map( int,  input().split() )

yellows = 0
greens = 0
correct = [[0]*3 for i in range(3)]
guess = [[0]*3 for i in range(3)]
c, g = defaultdict(int), defaultdict(int)
for i in range(3):
    correct[i][0], correct[i][1], correct[i][2] = input()

for i in range(3):
    guess[i][0], guess[i][1], guess[i][2] = input()

for i in range(3):
    for j in range(3):
        c[correct[i][j]] += 1
        g[guess[i][j]] += 1

for i in range(3):
    for j in range(3):
        if correct[i][j] == guess[i][j]:
            greens += 1
            c[correct[i][j]] -= 1
            g[correct[i][j]] -= 1

for a in c:
    if a in g:
        yellows += min(c[a], g[a])
        c[a] = 0

print(greens)
print(yellows)



