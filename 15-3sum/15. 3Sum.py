class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums) - 1

            while l<r:
                threesum = n + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    while nums[r] == nums[r+1] and l<r:
                        r -= 1

        
        return res