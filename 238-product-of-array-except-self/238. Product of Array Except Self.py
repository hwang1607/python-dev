class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        templeft = 1
        for i in range(1, len(nums)):
            templeft = nums[i-1] * templeft
            res[i] = templeft
        print(res)

        tempright = 1
        for i in range(len(nums) - 2, -1, -1):
            tempright = nums[i+1] * tempright
            res[i] *= tempright


        # for i in range(len(nums)):
        #     res[i] = left[i] * right[i]

        print(left, right)
        return res
            
        

        

            
        