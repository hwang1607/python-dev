class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # O((size of nums) * (total of all nums))
        dp = {} #index, total -> num of ways

        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            if (i, total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = dfs(i+1, total - nums[i]) + dfs(i+1, total + nums[i])

            return dp[(i, total)]
        
        return dfs(0,0)
        