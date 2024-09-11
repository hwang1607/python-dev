class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)

        for r in range(1, len(matrix)):
            for c in range(len(matrix)):
                left = matrix[r-1][c-1] if c > 0 else float("inf")
                mid = matrix[r-1][c]
                right = matrix[r-1][c+1] if c + 1 < len(matrix) else float("inf")
                matrix[r][c] += min(left, mid, right)

        return min(matrix[-1])
        