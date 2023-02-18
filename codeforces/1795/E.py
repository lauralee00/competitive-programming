import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


def solve():
    t, = read()
    for _ in range(t):
        n, = read()
        H = list(read())
        # find the maximum mp continuous peaks (local max)
        res = defaultdict(list)
        total_mp = sum(H)
        q = deque()
        seen = set()
        min_mp = float('inf')
        if n == 1:
            print(H[0])
            continue
        for i in range(n-1):
            if H[i] >= H[i+1]:
                q.append((i, i, True, True, 0,  H[i]))
        if H[-1] >= H[-2]:
            q.append((n-1, n-1, True, True, 0, H[n-1]))

        while q:
            # print(q[0])
            sidx, eidx, start, end, mp_saved, starting_mp = q.popleft()
            if (sidx, eidx, start, end) in seen: continue
            seen.add((sidx, eidx, start, end))
            saved_end = saved_start = 0
            if sidx == eidx:
                left_mp = right_mp = H[sidx]
            else:
                left_mp = H[sidx+1]-1
                right_mp = H[eidx-1]-1
            if not left_mp and right_mp or not start and not end:
                # print('def', total_mp , mp_saved, starting_mp)
                mp_cost = total_mp - mp_saved + starting_mp
                res[mp_cost].append((sidx, eidx))
                min_mp = min(min_mp, mp_cost)
                continue
            if start:
                # print(sidx)
                # print("ss", starting_mp, H[sidx])
                saved_start = min(left_mp, H[sidx])
                # if monster at sidx is killed and is not the leftmost
                # increase the explosion radius by 1 to the left

                if sidx > 0 and not H[sidx]-saved_start:
                    sidx -= 1
                else:
                    start = False
            
            if end:
                saved_end = min(right_mp, H[eidx])
                if eidx < n-1 and not H[eidx]-saved_end:
                    eidx += 1
                else:
                    end = False

            # TODO: remember that changed variable values during iteration can fuck up conditions like below
            mp_saved += (saved_end + saved_start if left_mp != starting_mp and right_mp != starting_mp else saved_end)

            # print('abc', mp_saved, saved_end, saved_start)
            if (sidx, eidx, start, end) not in seen:
                q.append((sidx, eidx, start, end, mp_saved, starting_mp))
        # print(res)
        print(min_mp)





if __name__ == '__main__':
    solve()
