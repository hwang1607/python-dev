class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        #curmin = min so far, curmax = max so far

        for n in nums:
            temp = n * curmax
            curmax = max(n, n * curmax, n * curmin)
            curmin = min(n, temp, n * curmin)
        
            res = max(res, curmax)
        
        return res
        