from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down:
        # TC: O(2^N)
        wordDict = set(wordDict)
        @lru_cache
        def recurse(word):
            if word in wordDict: return True
            for i, c in enumerate(s, start=1):
                firstWord, secWord = word[:i], word[i:]
                if firstWord in wordDict and secWord in wordDict:
                    return True
                else:
                    if firstWord in wordDict:
                        if recurse(secWord): return True
             return False
        return recurse(s)

        # bottom up:
        # TC: O( N^2 * M)
        # SC: O( N )
        dp = [False] * (len(s) + 1)
        dp[-1] = True  # if we can ever get beyond the last index at i = len(s), it's True
        for i in range(len(s), -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
        return dp[0]

