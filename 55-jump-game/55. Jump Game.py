class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[len(nums) - 1] = True


        for i in range(len(nums) -2, -1, -1):
            for j in range(nums[i] + 1):
                if i + j < len(nums) and memo[i+j]:
                    memo[i] = True
                    break

        return memo[0]
