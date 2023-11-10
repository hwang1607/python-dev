"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nmap = {None:None}

        temp = head
        while temp:
            new = Node(temp.val)
            nmap[temp] = new

            temp = temp.next
        
        temp = head
        while temp:
            new = nmap[temp]
            new.next = nmap[temp.next]

            new.random = nmap[temp.random]

            temp = temp.next
        
        return nmap[head]