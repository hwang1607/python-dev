class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        currmax = 0
        res = 0

        def dfs(r,c):

            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            nonlocal currmax
            grid[r][c] = 0
            print(currmax, r,c )
            currmax += 1

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        
        for r in range(rows):
            for c in range(cols):             
                res = max(res, dfs(r,c))
                currmax = 0

        return res
            



        