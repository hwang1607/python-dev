class HitCounter:

    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        
        while timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        

    def getHits(self, timestamp: int) -> int:
        if not self.hits:
            return 0
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)