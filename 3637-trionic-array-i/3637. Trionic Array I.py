class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # need at least 4 numbers to form up, down, up
        if n < 4:
            return False
        
        i = 0
        
        # -------------------------
        # Phase 1: strictly increasing
        # -------------------------
        up_start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        # must have moved at least once
        if i == up_start:
            return False
        
        # -------------------------
        # Phase 2: strictly decreasing
        # -------------------------
        down_start = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        
        # must have moved at least once
        if i == down_start:
            return False
        
        # -------------------------
        # Phase 3: strictly increasing again
        # -------------------------
        up2_start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        # must have moved at least once
        if i == up2_start:
            return False
        
        # must consume entire array exactly
        return i == n - 1