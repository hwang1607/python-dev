class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        a = 1
        b = 1

        for i in range(1, len(s)): # index 0 already determined to be possible
            cur = 0
            if s[i] != "0":
                cur = b
            
            doubledigit = int(s[i-1:i+1])
            if doubledigit >= 10 and doubledigit <=26:
                cur += a
            a = b
            b = cur
        
        return b