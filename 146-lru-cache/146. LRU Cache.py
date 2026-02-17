class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} #key to NODE
        self.head = Node(0,0) #dummy
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        usednode = self.dic[key]

        #remove it
        left = usednode.prev
        right = usednode.next
        left.next = right
        right.prev = left

        #put it at front
        self.head.next.prev = usednode
        usednode.next = self.head.next
        self.head.next = usednode
        usednode.prev = self.head

        
        
        
        
        
        
        
        return self.dic[key].val

        

    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            curr = self.dic[key]
            curr.val = value
            newnode = curr


            left = newnode.prev
            right = newnode.next
            left.next = right
            right.prev = left

        else:
            newnode = Node(key,value)

        self.dic[key] = newnode

        self.head.next.prev = newnode
        newnode.next = self.head.next
        self.head.next = newnode
        newnode.prev = self.head


        if len(self.dic) > self.capacity:
            #evict
            key = self.tail.prev.key



            self.dic.pop(key)
            new_last = self.tail.prev.prev
            new_last.next = self.tail
            self.tail.prev = new_last
            



        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)