class Solution:
    def trap(self, height: List[int]) -> int:
        l2r = [0] * len(height)
        r2l = [0] * len(height)

        leftmax = 0
        for i in range(len(height)):
            leftmax = max(leftmax, height[i])
            l2r[i] = leftmax

        rightmax = 0
        for i in range(len(height) - 1, -1, -1):
            rightmax = max(rightmax, height[i])
            r2l[i] = rightmax

        
        res = 0

        for i in range(len(height)):
            res += min(l2r[i], r2l[i]) - height[i]

        return res
