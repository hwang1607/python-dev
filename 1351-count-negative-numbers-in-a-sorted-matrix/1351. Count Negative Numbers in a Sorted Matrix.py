class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        c = 0
        r = ROWS - 1

        while r >= 0:
            while c < COLS:
                if grid[r][c] < 0:
                    count += COLS - c
                    break
                c+=1
            r -= 1

        return count
        