class Solution:
    def __init__(self):
        pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        
        for i in range(len(nums)):
            if target - nums[i] in m:
                return i,m[target - nums[i]]
            else:
                m[nums[i]] = i                