class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = collections.deque()
        time = 0
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r,c))

        while rotten and fresh > 0:
            time += 1
            
            length = len(rotten)
            for i in range(len(rotten)):
                r,c = rotten.popleft()


                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                print(r,c)

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1 :
                        rotten.append((row,col))
                        fresh -= 1
                        grid[row][col] = 2
                        print(rotten, fresh)
            

        

        if fresh == 0:
            return time

        return -1
        