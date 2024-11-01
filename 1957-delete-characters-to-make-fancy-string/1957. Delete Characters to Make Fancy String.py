class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 2:
            return s
        prev1 = s[0]
        prev2 = s[1]
        

        res = s[0] + s[1]

        for i in range(2, len(s)):
            if prev1 == prev2 == s[i]:
                pass
            else:
                res += s[i]
            prev1 = prev2
            prev2 = s[i]


        return res

            
        