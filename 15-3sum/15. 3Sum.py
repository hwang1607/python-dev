class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            if i > 0 and nums[i-1] == nums[i]: #the same number
                continue
            
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1 #same number
        
        return res
        