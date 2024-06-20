class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        sides = set()
        sides.add(dist(tuple(p1), tuple(p2)))
        sides.add(dist(tuple(p1), tuple(p3)))
        sides.add(dist(tuple(p1), tuple(p4)))
        sides.add(dist(tuple(p2), tuple(p3)))
        sides.add(dist(tuple(p2), tuple(p4)))
        sides.add(dist(tuple(p3), tuple(p4)))
    
        
        if 0 in sides:
            return False
        if len(sides) == 2:
            return True