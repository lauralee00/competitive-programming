from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # logs[i] = [IDi, timei]: user with ID_i performed an action at the minute time_i.
        # UAM: number of unique minutes which user performed action on leetcode (counted once per one active minute)
        # calculate answer[] where len(answer) = k, s.t. for 1 <= j <= k, answer[j] = num of users where UAM == j

        # findings: if user committed multiple actions in given time, disregard
        userTime = defaultdict(set)
        UAM_per_user = dict()
        answer = [0] * k

        for ID, time in logs:
            userTime[ID].add(time)

        for ID in userTime:
            uam = len(userTime[ID])
            UAM_per_user[uam] = UAM_per_user.get(uam, 0) + 1
            # if UAM not in UAM_per_user:
            #    UAM_per_user[UAM] = 0
            # else:
            #    UAM_per_user[UAM] += 1

        for j in range(1, k + 1):
            if j in UAM_per_user:
                answer[j - 1] = UAM_per_user[j]

        return answer
