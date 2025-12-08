class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = []
        maxneeded = 0
        curr = 0

        for start, end in intervals:
            arr.append([start, 1])
            arr.append([end, -1])
        
        arr.sort()

        for t,x in arr:
            curr += x
            maxneeded = max(maxneeded, curr)
        
        return maxneeded


            
        