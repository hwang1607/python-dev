class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : x[1])

        cur = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < cur[1]:
                res += 1
            else:
                cur = intervals[i]
        
        return res
        