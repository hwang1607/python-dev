class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {} #(r,c) : val

        def dfs(r, c, preval):
            if r >= ROWS or c >= COLS or c < 0 or r < 0:
                return 0
            if matrix[r][c] <= preval:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            
            currval = matrix[r][c]

            res = 1
            res = max(res, 1 + dfs(r+1,c, currval))
            res = max(res, 1 + dfs(r-1,c, currval))
            res = max(res, 1 + dfs(r,c+1, currval))
            res = max(res, 1 + dfs(r,c-1, currval))

            dp[(r,c)] = res

            return res



        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, -1)
        
        return max(dp.values())
        
        