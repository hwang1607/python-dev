class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def helper(dist):
            #count total num of pairs with diff <= dist
            l = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r-l # num of new pairs
            return res

        l, r = 0, max(nums) #differences between pairs must be within these

        while l<r:
            m = l + (r-l)//2

            pairs = helper(m)
            if pairs >= k:
                r = m #not minus 1
            else:
                l = m + 1
        return r        