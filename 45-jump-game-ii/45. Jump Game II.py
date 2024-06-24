class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = [float("inf")] * len(nums)
        memo[len(nums) - 1] = 0

        for i in range(len(nums) -1, -1, -1):
            for j in range(nums[i] + 1):
                if i + j < len(nums) and memo[i+j] != float("inf"):
                    memo[i] = min(memo[i], memo[i+j] + 1)

        print(memo)
        return memo[0]
                
