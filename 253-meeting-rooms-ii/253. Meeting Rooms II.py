class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        startpointer = 0
        endpointer = 0

        roomsneeded = 0

        while startpointer< len(intervals):
            if starts[startpointer] >= ends[endpointer]: #they dont overlap
                roomsneeded -=1
                endpointer +=1
            roomsneeded += 1
            startpointer +=1
        
        return roomsneeded

        