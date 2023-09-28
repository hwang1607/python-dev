class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1

        maxarea = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxarea = max(maxarea, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxarea
            
        