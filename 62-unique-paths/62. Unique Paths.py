class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for r in range(m-1):
            newrow = [1] * n

            for c in range(n - 2, -1, -1):
                newrow[c] = row[c] + newrow[c+1]

            row = newrow
        
        return row[0]
        