class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = [False] * len(nums)

        arr[-1] = True

        for i in range(len(nums) - 2, - 1, -1):
            for j in range(nums[i] + 1):
                if i+j >= len(nums):
                    break
                if arr[i+j] == True:
                    arr[i] = True
                    break
        return arr[0]
        