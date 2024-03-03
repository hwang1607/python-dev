class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        lr = [0,0]

        def check(l,r):
            nonlocal reslen

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r-l+1) > reslen:
                    reslen = (r-l+1)
                    lr[0] = l
                    lr[1] = r
                l -= 1
                r += 1
        
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        
        print(lr)
        return s[lr[0]:lr[1] + 1]


        