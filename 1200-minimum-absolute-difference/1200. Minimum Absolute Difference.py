class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float("inf")
        res = []
        
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff < mindiff:
                mindiff = diff
        
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff == mindiff:
                res.append([arr[i-1], arr[i]])
        
        return res






        