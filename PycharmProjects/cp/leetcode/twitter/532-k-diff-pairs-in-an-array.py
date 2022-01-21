from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # O(N^2) - TLE

        # seen = set()
        # nums.sort()
        # count, n = 0, len(nums)
        # for i in range(n):
        #     first = nums[i]
        #     for j in range(i+1, n):
        #         sec = nums[j]
        #         if (first, sec) not in seen and abs(first-sec) == k:
        #             count += 1
        #             seen.add((first, sec))
        # return count

        # O(N) time & space
        seen = set()
        seen_pairs = set()
        nums.sort()
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            if seen:
                if n + k in seen:
                    seen_pairs.add((n, n + k))
                elif n - k in seen:
                    seen_pairs.add((n, n - k))

                # if n in seen:
                #     continue

                # can't add this as there are same num pair (1, 1) that result in target diff of 0

            seen.add(nums[i])
        return len(seen_pairs)
