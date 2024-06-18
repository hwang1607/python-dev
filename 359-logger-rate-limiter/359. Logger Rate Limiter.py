class Logger:

    def __init__(self):
        self.seen = {} #msg : timestamp
        self.q = deque()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and timestamp - self.q[0][1] >= 10:
            del self.seen[self.q[0][0]]
            self.q.popleft()

        if message in self.seen:
            return False
        
        self.seen[message] = timestamp
        self.q.append((message, timestamp))
        return True
        