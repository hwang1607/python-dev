"""
This solution uses a Hash Set to store unique island shapes. Each island is converted
to a canonical representation and added to the set. The size of the set gives the
number of distinct islands.
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distinctIslands = set()

        # Define DFS function to explore islands
        def dfs(row, col, direction):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 0  # Mark as visited
                path.append(direction)
                dfs(row + 1, col, 'D')
                dfs(row - 1, col, 'U')
                dfs(row, col + 1, 'R')
                dfs(row, col - 1, 'L')
                path.append('0')  # Backtrack

        # Iterate through the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    path = []
                    dfs(row, col, 'S')  # Start exploration
                    distinctIslands.add(''.join(path))

        # Return the number of distinct islands
        return len(distinctIslands)