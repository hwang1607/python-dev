class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                del nums[i+1]