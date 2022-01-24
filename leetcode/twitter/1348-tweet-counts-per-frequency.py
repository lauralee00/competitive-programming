from collections import defaultdict
from typing import List


class TweetCounts:

    def __init__(self):
        self.tweet = defaultdict(list)  # [(time, )]

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet[time].append(tweetName)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        unit = {"minute": 60, "hour": 3600, "day": 86400}
        res = []

        for i in range(startTime, endTime + 1, unit[freq]):
            interval = 0

            for j in range(i, min(i + unit[freq], endTime + 1)):
                if j in self.tweet and tweetName in self.tweet[j]:
                    interval += self.tweet[j].count(tweetName)  # can't add len, can only add the count of that tweetname

            res.append(interval)

        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)