class Solution:
    def trap(self, height: List[int]) -> int:

        leftmax = height[0]
        rightmax = height[-1]
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            if height[l] <= height[r]:
                leftmax = max(leftmax, height[l])
                print(leftmax, rightmax, l, r)
                res += leftmax - height[l]
            
                l += 1
            else:

                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
            
                r -= 1
        
        return res