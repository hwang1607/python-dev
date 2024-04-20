class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        curr = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] > curr[1]: #not intersecting
                res.append(curr)

                curr = intervals[i]
            else: #intersecting
                curr[1] = max(curr[1], intervals[i][1])
        
        res.append(curr)
    
        return res
        