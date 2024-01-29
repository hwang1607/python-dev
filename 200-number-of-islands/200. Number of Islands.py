class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        res = 0

       
        def bfs(r,c):
            #visit.add((r,c))
            grid[r][c] = 0

            # if r+1 in range(ROWS) and c in range (COLS) and grid[r+1][c] == "1" and (r+1,c) not in visit:
            #     bfs(r+1,c) 

            # if r in range(ROWS) and c+1 in range (COLS) and grid[r][c+1] == "1" and (r,c+1) not in visit:
            #     bfs(r,c+1)

            # if r-1 in range(ROWS) and c in range (COLS) and grid[r-1][c] == "1" and (r-1,c) not in visit:
            #     bfs(r-1,c)

            # if r in range(ROWS) and c-1 in range (COLS) and grid[r][c-1] == "1" and (r,c-1) not in visit:
            #     bfs(r,c-1)

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if r+dr in range(ROWS) and c+dc in range (COLS) and grid[r+dr][c+dc] == "1" and (r+dr,c+dc) not in visit:
                    bfs(r + dr, c + dc)
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    res += 1
        return res
        