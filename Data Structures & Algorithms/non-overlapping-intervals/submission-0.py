class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0
        intervals.sort(key=lambda x: x[0])

        if len(intervals) == 0:
            return 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                removals += 1
                prev_end = min(intervals[i][1], prev_end)
            else:
                prev_end = intervals[i][1]
            
        return removals