class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        res = 0
        factor = 2

        while n>1:
            while n%factor == 0:
                n //= factor
                res += factor
            factor += 1
            #print(n, res)

        return res
        