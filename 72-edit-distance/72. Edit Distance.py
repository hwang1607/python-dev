class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} #i,j : operations

        if not word1 or not word2:
            return max(len(word1), len(word2))



        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            
            res = float("inf")
            res = min(res, 1 + dfs(i+1, j+1)) #replace
            res = min(res, 1 + dfs(i+1, j)) #delete
            res = min(res, 1 + dfs(i, j+1)) #insert

            dp[(i,j)] = res

            return res
            

        
        return dfs(0,0)
        