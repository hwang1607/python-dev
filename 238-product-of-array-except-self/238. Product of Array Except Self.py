class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))


        for i in range(len(nums)-1):
            res[i+1] = nums[i] * res[i]
    
        prevvalue = 1
        for i in range(len(nums) - 1, 0, -1):
            prevvalue *= nums[i]
            res[i-1] *= prevvalue



        return res
