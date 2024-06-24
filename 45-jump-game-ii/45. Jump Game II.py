class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        
        return jumps


        # dp = [float("inf")] * len(nums)
        # dp[-1] = 0

        # for i in range(len(nums) - 2, -1, -1):
        #     for j in range(nums[i] + 1):
        #         if i+j < len(nums):
        #             dp[i] = min(dp[i], 1 + dp[i+j])
        
        # return dp[0]

