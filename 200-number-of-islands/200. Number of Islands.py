class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0
        visited = set()

        def bfs(row, col):
            queue = deque([(row, col)])

            visited.add((row,col))

            while queue:
                currow, curcol = queue.popleft()
                directions = [(-1,0), (1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    newrow, newcol = currow + dr, curcol + dc

                    if (newrow in range(rows) and newcol in range(cols) and grid[newrow][newcol] == "1" and (newrow, newcol) not in visited):
                        queue.append((newrow, newcol))
                        visited.add((newrow, newcol))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
        
        return res
        
        