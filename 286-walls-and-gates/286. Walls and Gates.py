class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visit = set()
        q = deque()
        dist = 0


        for r in range(ROWS): #find gates
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if dist < rooms[r][c]:
                    rooms[r][c] = dist
                
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and rooms[row][col] != -1 and (row,col) not in visit:
                        visit.add((row,col))
                        q.append((row,col))
                
            dist += 1


        