class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l)//2
            
            count = 0
            for num in nums:
                if num <= m:
                    count += 1
            if count > m:
                r = m
            else:
                l = m + 1
        return l
        