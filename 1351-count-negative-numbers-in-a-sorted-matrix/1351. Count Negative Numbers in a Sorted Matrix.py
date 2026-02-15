class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        c = 0

        for r in range(ROWS-1, -1, -1):
            while c < COLS:
                print(r,c)
                if grid[r][c] < 0:
                    count += COLS - c
                    break
                c+=1

        return count
        
        