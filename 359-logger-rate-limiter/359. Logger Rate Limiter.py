class Logger:

    def __init__(self):
        self.seen = {} #msg, time
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.seen:
            prev_time = timestamp - 10
            if self.seen[message] > prev_time:
                return False
            self.seen[message] = timestamp
        else:
            self.seen[message] = timestamp


        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)