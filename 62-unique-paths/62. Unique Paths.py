class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        row[n-1] =1

        for i in reversed(range(m)):
            #newrow = [1] * n
            for j in range(n-2, -1, -1):
                #newrow[j] = newrow[j+1] + row[j]
            
                row[j] = row[j] + row[j+1]
            
            #row = newrow



        return row[0]
        