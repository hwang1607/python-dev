class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cursum = 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            ans = max(ans, cursum)
        return ans
        