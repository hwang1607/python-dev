class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            if i > 0 and nums[i-1] == nums[i]:
                continue

            while l<r:

                threesum = nums[i] + nums[l] + nums[r]
                
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res