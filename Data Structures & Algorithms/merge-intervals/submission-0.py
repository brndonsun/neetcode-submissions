class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0] )
        result = []
        last_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= last_interval[1]: #if overlap
                last_interval[0] = min(intervals[i][0], last_interval[0])
                last_interval[1] = max(intervals[i][1], last_interval[1])
            else:
                result.append(last_interval)
                last_interval = intervals[i]

        result.append(last_interval)
        return result


            
        