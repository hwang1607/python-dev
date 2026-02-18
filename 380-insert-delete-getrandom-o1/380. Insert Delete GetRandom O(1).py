class RandomizedSet:

    def __init__(self):
        self.hmap = {} #value to index
        self.arr = []
        

    def insert(self, val: int) -> bool:

        if val in self.hmap:
            return False
        
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False

        i = self.hmap[val]
        lastval = self.arr[-1]

        #overwrite the index of where the last vaue was with the index of the value to be deleted
        #this is because i dont care about the index of the to be deleted value is 
        #and the position of the last val is now the postion of the value to be deleted
        self.hmap[lastval] = i
        del self.hmap[val]
        
        #put the last VALUE over on top of the to be deleted value
        self.arr[i] = lastval
        self.arr.pop()

        return True

        

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()