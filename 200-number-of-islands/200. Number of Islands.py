class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        seen = set()


        def dfs(r,c):
            #grid[r][c] = "0" #marks it as seen
            seen.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr,dc in directions:
                newrow = r + dr
                newcol = c + dc

                if 0 <= newrow < ROWS and 0 <= newcol < COLS and grid[newrow][newcol] == "1" and (newrow,newcol) not in seen:
                    dfs(newrow, newcol)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    res += 1
        return res