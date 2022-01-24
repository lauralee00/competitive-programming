# https://atcoder.jp/contests/abc234/tasks/abc234_d

# find array up to the k-1th index
N, K = map(input().split())
P = [input() for _ in range(N)]
import heapq
P_to_K = P[K-1:]
P_to_K.sort()
new = [0]*N
ticker = 0
not_seen = []
for i in range(1, N+1):
    if i == P_to_K[ticker]:
        new[i-1] = i
        ticker += 1
    elif i < P_to_K[ticker]:
        heapq.heappush(not_seen, i)
    elif i > P_to_K[ticker]


    if i == P_to_K[ticker]:
    new
    i += 1
        new += i in range(P_to_K):

seen = []
for i in range(1, K+1):
    heapq.heappush(seen, i)
    if P[i] == i:
        print(i)


        P_to_K
    num = i+1

heapq.heapify(P_to_K)
for i in range(K, N):
    heapq.haP_to_K += P[i]
    #heap