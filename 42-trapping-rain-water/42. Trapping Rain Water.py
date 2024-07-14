class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = height[0]
        maxright = height[-1]

        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            if maxleft < maxright:
                l+=1
                maxleft = max(maxleft, height[l])
                res += maxleft - height[l]
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += maxright - height[r]

                

        return res
            
        
        