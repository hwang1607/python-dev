class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
       
        def bfs(r,c):
            grid[r][c] = 0

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if r+dr in range(ROWS) and c+dc in range (COLS) and grid[r+dr][c+dc] == "1":
                    bfs(r + dr, c + dc)
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        return res
        