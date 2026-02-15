class HitCounter:

    def __init__(self):
        self.counts = deque() #timestamp, hits
        

    def hit(self, timestamp: int) -> None:
        self.counts.append(timestamp)

        start = timestamp - 300
        if start < 0:
            start = 0
        while self.counts[0] <= start:
            self.counts.popleft()

        

    def getHits(self, timestamp: int) -> int:
        res = 0
        start = timestamp - 300
        if start < 0:
            start = 0
        
        while self.counts and self.counts[0] <= start:
            self.counts.popleft()

        res = len(self.counts)
        
        return res

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)