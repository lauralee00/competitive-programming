from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        occupied_idx = [] # space O(N)
        a, b = 0, len(seats) - 1
        mindist = [-1] * len(seats) # space O(N)

        while a < len(seats):  # time O(N)

            if seats[a]:
                occupied_idx.append(a)

            recent = occupied_idx[-1] if occupied_idx else float("-inf")
            mindist[a] = a - recent
            a += 1

        occupied_idx = []  # space O(N), cleanup ( reverse sorting makes it O (n log n) )

        while b >= 0:  # time O(N)

            if seats[b]:
                occupied_idx.append(b)

            recent = occupied_idx[-1] if occupied_idx else float("+inf")
            mindist[b] = min(mindist[b], recent - b)  # take min distance between left and right pass to find closest
            b -= 1

        return max(mindist)  # return max of min distance