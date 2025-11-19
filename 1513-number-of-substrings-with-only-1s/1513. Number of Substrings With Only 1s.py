class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        mod = 10**9 + 7

        cons = 0

        for c in s:
            if c == "1":
                cons += 1
                res = (res + cons) % mod
            else:
                cons = 0

        return res
             