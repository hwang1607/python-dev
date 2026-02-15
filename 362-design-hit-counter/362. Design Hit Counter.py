class HitCounter:

    def __init__(self):
        self.counts = {} #timestamp, hits
        

    def hit(self, timestamp: int) -> None:
        self.counts[timestamp] = self.counts.get(timestamp, 0) + 1

        

    def getHits(self, timestamp: int) -> int:
        res = 0
        start = timestamp - 300
        if start < 0:
            start = 0

        for i in range(start + 1, timestamp + 1):
            if i in self.counts:
                res += self.counts[i]
        # for key in self.counts:
        #     if start < key <= timestamp:
        #         res += self.counts[key]
        
        return res

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)