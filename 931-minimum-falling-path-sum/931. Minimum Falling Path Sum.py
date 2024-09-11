class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [0] * (len(matrix)) #row below

        for r in matrix[::-1]:
            temparr = [0] * (len(matrix)) 
            for i, n in enumerate(r):
                temparr[i] = n + min(dp[i-1] if i > 0 else float("inf"), dp[i], dp[i+1] if i+1 < len(matrix) else float("inf"))
            dp = temparr

        return min(dp)