class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visit = set()
        minheap = [(grid[0][0], 0, 0)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit.add((0,0))

        #bfs
        while minheap:
            cost,r,c = heapq.heappop(minheap)
            #print(r,c)
            if r == n-1 and c == n-1:
                return cost
           
            for dr, dc in directions:
                nRow = r + dr
                nCol = c + dc

                if nRow in range(n) and nCol in range(n) and (nRow,nCol) not in visit:
                    heapq.heappush(minheap, (max(cost, grid[nRow][nCol]),nRow,nCol))
                    visit.add((nRow, nCol))
                



        