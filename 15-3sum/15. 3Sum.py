class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            if i>0 and nums[i] == nums[i-1]: #skip if its the same number i
                continue

            while l<r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l] , nums[r]])
                    l+=1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]: #skip if its the same number l
                        l+=1
        
        return res
        