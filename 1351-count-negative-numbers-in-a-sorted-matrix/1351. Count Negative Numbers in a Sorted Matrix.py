class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        first_neg_col = 0
        r = ROWS - 1

        while r >= 0:
            while first_neg_col < COLS and grid[r][first_neg_col] >= 0:
                first_neg_col += 1
            count += COLS - first_neg_col
            r-=1
        return count
    