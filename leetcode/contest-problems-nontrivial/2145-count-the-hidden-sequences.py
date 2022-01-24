import itertools
from typing import List

# TC: O(N)
# SC: O(N)

# chad code:

class Solution:  # O(N)
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # iterable of cum sum of differences with a leading [0] of len(diff) + 1 ---> takes care of edge case of 1 diff
        a = list(itertools.accumulate(differences), initial=0)  # probably O(N)
        return max(0, upper - lower - (max(a) - min(a)) + 1)    # also O(N)

        # alternate (without adding a "0" element, need to account for differences in min and max)

        # a = list(itertools.accumulate(differences))  # cumulative sum of items in differences
        # return max(0, upper - lower - (max(max(a), 0) - min(min(a), 0)) + 1)

# my shit code:

# class Solution:
#     def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
#         locMin = locMax = 0
#         cumMin, cumMax = 0, 0
#
#         for difference in differences:
#             locMin += difference
#             cumMin = min(locMin, cumMin)
#         for difference in differences:
#             locMax += difference
#             cumMax = max(locMax, cumMax)
#             # print(cumMax)
#
#         diff = cumMax - cumMin
#         # print(cumMax, cumMin)
#
#         if lower + diff > upper:
#             return 0
#         else:
#             return upper - (lower + diff) + 1
