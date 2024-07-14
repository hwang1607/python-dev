class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * len(height)
        maxright = [0] * len(height)
        res = 0

        maxleft[0] = height[0]
        for i in range(1, len(height)):
            maxleft[i] = max(height[i], maxleft[i-1])

        maxright[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            maxright[i] = max(height[i], maxright[i+1])

        for i in range(len(height)):
            water = min(maxleft[i], maxright[i])
            res += water - height[i]

        return res
            
        
        