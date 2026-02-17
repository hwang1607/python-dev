class TimeMap:

    def __init__(self):
        self.store = {} #key to dict of time and value
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]

        l = 0
        r = len(arr) - 1

        while l<=r:
            mid = (l+r)//2
            ts = arr[mid][0] 

            if ts <= timestamp: #yes its valid
                l = mid + 1
            else:
                r = mid - 1

        if r == -1:
            return ""
        return arr[r][1]


        

            
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)