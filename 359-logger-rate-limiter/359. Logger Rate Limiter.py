class Logger:

    def __init__(self):
        # key=message, val=last printed timestamp
        self.last_print = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_print:
            self.last_print[message] = timestamp
            return True
        # the message has occured before
        if timestamp < self.last_print[message] + 10: # within supressing time frame
            return False
        else:
            self.last_print[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)