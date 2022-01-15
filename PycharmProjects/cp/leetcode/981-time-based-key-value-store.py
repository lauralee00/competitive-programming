# https://leetcode.com/problems/time-based-key-value-store/
# py doc on bisect: https://docs.python.org/3/library/bisect.html

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.new = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.new[key]:
            self.new[key] = [(timestamp, value)]
        else:
            bisect.insort(self.new[key], (timestamp, value)) #O( log N search + N insertion  ) -> O( N )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.new: return ""
        temp_ts, temp_val = None, ""
        for (ts_prev, val) in self.new[key]: # O( N )
            if ts_prev > timestamp:
                break  # or return temp_val, but this is prettier given we don't have to case returns
            temp_ts, temp_val = ts_prev, val
        return temp_val
'''
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
