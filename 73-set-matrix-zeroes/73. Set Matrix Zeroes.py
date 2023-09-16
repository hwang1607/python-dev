class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        zeror = set()
        zeroc = set()


        # def makeZero(r,c):
        #     for r in range(rows):
        #         matrix
        #     for c in range(cols):
        


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeror.add(r)
                    zeroc.add(c)

        print(zeror)

        for r in zeror:
            for c in range(cols):
                matrix[r][c] = 0

        for r in range(rows):
            for c in zeroc:
                matrix[r][c] = 0
            


    
    
        