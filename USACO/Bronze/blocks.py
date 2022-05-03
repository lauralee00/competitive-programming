import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())



N = int(input())
D1 = set(map(str, input().split()))
D2 = set(map(str, input().split()))
D3 = set(map(str, input().split()))
D4 = set(map(str, input().split()))
wordList = []
for _ in range(N):
    wordList.append(input())

for w in wordList: #[COW, MOO, ZOO, MOVE, CODE] 1 <= N <= 10
    cand = defaultdict(set)
    word = [False]*len(w)
    for i, l in enumerate(w): #C O W in "COW"
        if l in D1:
            cand[i].add(1)
        if l in D2:
            cand[i].add(2)
        if l in D3:
            cand[i].add(3)
        if l in D4:
            cand[i].add(4)

    def dfs(seenDice, seenIdx):
        if len(seenDice) == 4 and seenIdx == len(w): return True
        for i in cand:
            if i in seenIdx: continue
            seenIdx.add(i)
            for dice in cand[i]:
                if dice not in seenDice:
                    seenDice.add(dice)
                    dfs(seenDice, seenIdx)
                else:
                    continue
                seenDice.remove(dice)
            seenIdx.remove(i)
        return False

    seenDice = set()
    seenIdx = set()

    if dfs(seenDice, seenIdx): print("YES")
    else: print("NO")














