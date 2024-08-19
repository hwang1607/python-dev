class Solution:
    def mySqrt(self, x: int) -> int:

        l = 1
        r = x
        if x == 0 :
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
        