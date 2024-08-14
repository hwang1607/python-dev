class UndergroundSystem:

    def __init__(self):
        self.ontrip = {} #customer id: (station name, left time)
        self.times = defaultdict(lambda : [0,0]) #(station1, station2) :  now the default val is [0,0] [total time, num of entries]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ontrip[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station1, leftTime = self.ontrip[id]
        self.times[(station1, stationName)][0] += t-leftTime
        self.times[(station1, stationName)][1] += 1

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.times[(startStation,endStation)]
        return totalTime / totalTrips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)