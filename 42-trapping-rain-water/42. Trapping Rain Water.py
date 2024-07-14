class Solution:
    def trap(self, height: List[int]) -> int:

        leftmax = 0
        rightmax = 0
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            if height[l] <= height[r]:
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            
                l += 1
            else:
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
            
                r -= 1
        
        return res