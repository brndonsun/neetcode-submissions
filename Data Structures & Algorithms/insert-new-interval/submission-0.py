class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []
        newIntIn = False
        for interval in intervals:
            if newInterval[1] < interval[0]:
                if not newIntIn:
                    merged_intervals.append(newInterval)
                    newIntIn = True
                merged_intervals.append(interval)

            elif interval[1] < newInterval[0]:
                merged_intervals.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]


        if not newIntIn: merged_intervals.append(newInterval)
        
        return merged_intervals
