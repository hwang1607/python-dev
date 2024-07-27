class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtotal = nums[0]
        curr = 0

        for n in nums:
            curr += n
            maxtotal = max(maxtotal, curr)
            if curr < 0:
                curr = 0
    
        return maxtotal

            
            

        