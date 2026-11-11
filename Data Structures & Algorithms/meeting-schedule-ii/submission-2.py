"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #intuition: sort and check for overlaps, minimum amount of rooms
        # is the maximum number of overlaps are any point
        mp = defaultdict(int)
        for interval in intervals:
            start, end = interval.start, interval.end
            mp[start] += 1
            mp[end] -= 1

        res = []
        result = 0
        have = 0
        for i in sorted(mp):
            have += mp[i]
            result = max(result, have)

        return result



        # [40]
