# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

import sys
from collections import defaultdict
from typing import List

input = lambda: sys.stdin.readline().strip()
read = lambda: map(int, input().split())


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        pairs = 0
        seen = defaultdict(int)
        for i, t in enumerate(time):
            mod = t % 60
            seen[mod] += 1

        for mod, freq in seen.items():
            if mod == 0 or mod == 30:
                pairs += freq * (freq - 1)
            elif 60 - mod in seen:
                pairs += freq * seen[60 - mod]
        return pairs // 2  # double counting
