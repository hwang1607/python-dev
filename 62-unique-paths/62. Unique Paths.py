class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        row[n-1] =1

        for i in reversed(range(m)):
            for j in reversed(range(n-1)):
                row[j] = row[j] + row[j+1]
            
        return row[0]
        