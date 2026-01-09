class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalsum = 0

        minabsval = float("inf")
        negcount = 0

        for row in matrix:
            for val in row:
                totalsum += abs(val)
                if val < 0:
                    negcount += 1
                minabsval = min(minabsval, abs(val))
        
        if negcount % 2 != 0:
            res = totalsum - (2* minabsval)
            return res
            
        return totalsum