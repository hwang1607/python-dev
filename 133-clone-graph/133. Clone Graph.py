"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        l=[]
        p=[]
        def display(n):
            if(n):
                l.append(n.val)
                x=[]
                for i in n.neighbors:
                    x.append(i.val)
                p.append(x)
                for i in n.neighbors:
                    if(i.val not in l):
                        display(i)

        A=[]
        visited=[]        
        def clone(n):
            if(n):
                new=Node(n.val)
                visited.append(new.val)
                A.append(new)
                for i in n.neighbors:
                    if(i.val not in visited): 
                       
                        new.neighbors.append(clone(i))
                    else:
                        for j in A:
                            if(j.val==i.val):
                                new.neighbors.append(j)
                                break
                return new
        return clone(node)
        display(clone(node))
        print(p)
        