class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key to node :/
        self.cap = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self. left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #insert right
    def insert(self,node):
        prev = self.right.prev
        r = self.right
        r.prev = prev.next = node # pointing at node
        node.next, node.prev = self.right, prev #pointing from node


        # prev, nxt = self.right.prev, self.right
        # prev.next = nxt.prev = node
        # node.next, node.prev = nxt, prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            print(self.left.next.key)
            del self.cache[self.left.next.key]
            self.remove(self.left.next)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)