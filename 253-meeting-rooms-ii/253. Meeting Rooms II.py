class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        endtimes = []

        heapq.heappush(endtimes, intervals[0][1])

        for i in range(1, len(intervals)):
            if endtimes[0] <= intervals[i][0]: #meetings overlap
                heapq.heappop(endtimes)
            heapq.heappush(endtimes, intervals[i][1])
        
        return len(endtimes)