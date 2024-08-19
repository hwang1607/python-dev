class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = x
        if x <= 1:
            return x

        while l<=r:
            mid = l+(r-l)//2
            print(l,r)

            if mid == x//mid:
                return mid
            
            if mid < x // mid:
                l = mid+1
            else:
                r = mid-1
            
        
        return r
        