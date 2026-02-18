class RandomizedSet:
    #array can do get random
    #hashmap for complexity

    def __init__(self):
        self.arr = []
        self.hmap = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1

        return True
        

    def remove(self, val: int) -> bool:
        #removing the last element of an array is o(1)
        if val not in self.hmap:
            return False
        
        # print(self.arr, "asdf")
        idx = self.hmap[val]

        #swap indexes on map
        self.hmap[self.arr[idx]],  self.hmap[self.arr[-1]] =  self.hmap[self.arr[-1]],  self.hmap[self.arr[idx]]
        self.hmap.pop(val)

        #swap in array
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop() #value is removed

        return True


    def getRandom(self) -> int:
        # print(self.arr)
        return self.arr[randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()