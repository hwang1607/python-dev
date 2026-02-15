class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS):
                print(r,c)
                if grid[r][c] < 0:
                    count += COLS - c
                    break

        return count
        
        